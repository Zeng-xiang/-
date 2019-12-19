"""封装返回json数据的方法"""
import json
from django.conf import  settings
from django.http import  HttpResponse
"""
code data 每次都需要传递 所以可以优化 
"""
def render_json(code=0,data=None):
    dic = {
        'code': code,
        'data': data
    }
    # 调试时数据格式化
    if settings.DEBUG:
        dic_dumps = json.dumps(dic,ensure_ascii=False,indent=4,sort_keys=True)
    # 传输时 json 压缩
    else:
        dic_dumps = json.dumps(dic,ensure_ascii=False,separators=[',',':'])
    return HttpResponse(dic_dumps)