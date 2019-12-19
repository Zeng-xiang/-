from django.shortcuts import render

# Create your views here.
#前端的就已经处理了判断手机号的一切逻辑
from lib.http import render_json
from lib.sms import send_sms
from django.http import  JsonResponse
from common import  errors
def submit_phone(request):
    """提交手机号码,发送验证码"""
    phone = request.POST.get('phone')

    #因为别的地方可能也需要使用到验证码,可以给它封装成函数,以便使用
    # 发送验证码
    status,msg = send_sms(phone)  # 就是函数返回的两个值(eg: True,ok )
    if not status: #表示False
        # return JsonResponse({'code':errors.SMS_ERROR,'data':'短信发送失败'})
        return render_json(code=errors.SMS_ERROR,data='短信发送失败')
    #发送成功
    # return  JsonResponse({'code':0,'data':None})
    return render_json()