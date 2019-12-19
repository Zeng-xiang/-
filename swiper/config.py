"""
云之讯的地址  和我们原来项目没有关系 则写在sms不好,重新建立文件写依稀额外的配置
写一些模块
"""
#云之讯 的地址
# 按照云之讯的格式来写
YZX_URL = 'https://open.ucpaas.com/ol/sms/sendsms'
# APPID = '833b086cb62f40e4937cb7bef7e96c58'
# TOKEN =  "f81d1ce2210bccaf90f5d9f9b87ae3a6"
# SID = '442234d98d86a3413382b6aaf0211bfe'
# templateid=  "448535"  # 模板id  在模板库里面写的模板短信id

YZX_PARAMS = {
    "sid": "442234d98d86a3413382b6aaf0211bfe",
    "token": "f81d1ce2210bccaf90f5d9f9b87ae3a6",
    "appid": "833b086cb62f40e4937cb7bef7e96c58",
    "templateid": "448535",
    "param": None, # 不固定
    "mobile": None, # 不固定  手机号码
}