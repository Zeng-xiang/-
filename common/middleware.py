from django.utils.deprecation import  MiddlewareMixin

from lib.http import render_json
from common import  errors
from user.models import User


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        white_list = ['/api/zengxiang/submit/phone/','/api/login/submit/phone/']

        if request.path in white_list:
            return None
        uid = request.session.get('uid')
        if not uid:
            return render_json(code=errors.LOGIN_ERROR,data='请登录')
        user = User.objects.get(id=uid)
        request.user = user