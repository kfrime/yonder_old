"""
Django settings for iseek_backend project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os


# 更改默认的的数据库连接，否则会报错：
# django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
import pymysql
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '99mu4rt+l5lc(m5h!06p^*-s*-y6q1gxa_da+z5zdr*$jxp2ch'


ALLOWED_HOSTS = ['*']


# Application definition
# 添加了新的app需要重启服务器
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # 其他组件
    'mptt',     # 树形层次结构
    'rest_framework',
    'corsheaders',  # enable CORS

    # 自定义的 app
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


    # 自定义的Middleware
    'core.middleware.logs.LogMiddleware',
]

ROOT_URLCONF = 'iseek_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 设置视图
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'iseek_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 10
# }

PAGE_SIZE = 10

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# 设置登录和注册成功后重定向的页面，默认是/accounts/profile/
LOGIN_REDIRECT_URL = "/"

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False  # 关闭国际时间，不然数据库报错


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# 静态文件
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 媒体文件收集
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

PAGE_LIMIT = 5

# 导入个人的配置信息
from .base_settings import *

# log 配置
from .logs import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# enable CORS
# https://stackoverflow.com/questions/35760943/how-can-i-enable-cors-on-django-rest-framework
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
)
CORS_ORIGIN_REGEX_WHITELIST = (
    'localhost:8000',
)
