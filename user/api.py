import os

from django.shortcuts import render
from django.conf import settings
# Create your views here.
#前端的就已经处理了判断手机号的一切逻辑

from lib.http import render_json
from lib.qiniu import upload_qiniu

from lib.sms import send_sms

from django.http import  JsonResponse

from common import  errors

from django.core.cache import  cache

from common import  keys
from swiper import config
from user.logie import handle_upload
from user.models import User

from user.form import ProfileModelForm


def submit_phone(request):
    """提交手机号码,发送验证码"""
    phone = request.POST.get('phone')

    #因为别的地方可能也需要使用到验证码,可以给它封装成函数,以便使用
    # 发送验证码
    # status,msg = send_sms(phone)  # 就是函数返回的两个值(eg: True,ok )
    # if not status: #表示False
    #     # return JsonResponse({'code':errors.SMS_ERROR,'data':'短信发送失败'})
    #     return render_json(code=errors.SMS_ERROR,data='短信发送失败')
    # #发送成功
    # # return  JsonResponse({'code':0,'data':None})
    send_sms.delay(phone)
    return render_json()


def submit_vcode(request):
    """提交验证码"""
    phone = request.POST.get('phone')
    vcode = request.POST.get('vcode')  # 验证码

    #从缓存中取出vcode
    cached_vcode = cache.get(keys.VCODE_KEY % phone)
    print(cached_vcode)
    if vcode == cached_vcode:
        # #说明验证码正确,可以登录或者注册
        # try:
        #     user = User.objects.get(phonenum=phone)
        # except User.DoesNotExist:
        #     user = User.objects.create(phonenum=phone,nickname=phone)
        #     user.save()
        # #吧用户的id存入session,完成登录

        #优化
        #get_or_create 如果存在就返回,不存在就创建,defaults里面是创建的默认值

        # 是上面的优化
        user, _ = User.objects.get_or_create(phonenum=phone,defaults={'nickname':phone})
        print(user)
        request.session['uid'] = user.id

        return render_json(data=user.to_dict())
    else:
        #验证码错误
        return render_json(code=errors.VCODE_ERROR,data='验证码错误')
#
def get_profile(request):
    # uid = request.session.get('uid')
    # if not uid:
    #     return render_json(code=errors.LOGIN_ERROR, data='请登录')
    # user = User.objects.get(id=uid)
    print(request.user.profile.min_distance)
    return render_json(data=request.user.profile.to_dict())


def edit_profile(request):
    """修改个人资料"""
    form = ProfileModelForm(request.POST)
    if form.is_valid():
        #接受并且保存
        profile = form.save(commit=False )
        uid = request.session['uid']
        profile.id = uid
        profile.save()
        return render_json(data=profile.to_dict())
    # form本身就是个字典
    return render_json(code=errors.PORFILE_ERROR,data=form.errors)

# 个人头像上传
def upload_avatar(request):
    """上传个人头像照片"""
    #获取上传图片数据
    avatar = request.FILES.get('avatar')
    #保存到指定的位置
    # print(type(avatar))
    #分块写入本地
    user = request.user
    handle_upload.delay(user,avatar)
    return render_json(data='ok')