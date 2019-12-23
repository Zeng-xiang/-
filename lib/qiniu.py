from qiniu import Auth, put_file, etag
from swiper import config
#需要填写你的 Access Key 和 Secret Key
def upload_qiniu(filename,file_path):
    #构建鉴权对象
    q = Auth(config.AK, config.SK)
    #要上传的空间
    bucket_name = 'zengxiang0728'
    #上传后保存的文件名

    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, filename, 3600)
    #要上传文件的本地路径
    ret, info = put_file(token, filename, file_path)
    print(info)
    print(ret)