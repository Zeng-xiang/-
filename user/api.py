from django.shortcuts import render

# Create your views here.
def submit_phone(request):
    """提交手机号码,发送验证码"""
    phone = request.POST.get('phone')
    # 发送验证码
    