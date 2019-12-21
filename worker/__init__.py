"""每次调用worker里面的py文件的时候都会先进入到init.py里面来"""
"""则每次都会初始化"""
import os
from celery import Celery

from worker import config



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swiper.settings')

celery_app = Celery('swiper')
celery_app.config_from_object(config)
celery_app.autodiscover_tasks() #自动发现django项目里面的异步任务
