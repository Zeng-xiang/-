import random
# 验证码需要我们写
# 参数写成size = 4  是设置4位数的随机码,如果需要写成6位数验证码,也方便进行修改
import requests
from django.core.cache import cache  #django自带缓存 #默认存到内存
from common import keys
from swiper import config

from worker import  celery_app

def gen_vcode(size=4):
    start = 10 * (size - 1)
    end = 10 ** size - 1
    # randint 是全闭区间
    return str(random.randint(start, end))

@celery_app.task
def send_sms(phone):
# 我们通过 requests(可以直接发起请求) 来对云之讯发post请求
    params = config.YZX_PARAMS.copy()  #浅拷贝

    #设置缓存
    vcode = gen_vcode()
    print(vcode)
    params['mobile'] = phone  # 把字典手机号key 赋值

    #设置 缓存  并设置过期时间
    cache.set(keys.VCODE_KEY % phone,vcode,timeout=1800)

#直接赋值的话 会对原数据(字典:可变)发生改变  浅拷贝 因为是单层的,所以不会对原数据发生改变  以免其他需要用到验证码 其原数据发生改变了

    params['param'] = vcode  # 验证码
    resp = requests.post(config.YZX_URL,json=params)  # 直接post访问云之讯,并传递云之讯需要的json数据
    if resp.status_code == 200:  # 状态码
        #说明访问服务器没问题

        #能够把云之讯返回的所有数据拿到
        result = resp.json()
        if result['code'] == '000000':
            return True,'ok'
        else:
            return False,result['msg']
    else:
        return False,'访问短信服务器有误'