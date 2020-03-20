"""
Django settings for performance_management project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')&jkicxr9s2_6dgg1m*5rl-5yp@bo+k)+t^_iqq@(dmo7e2+v9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'performance.apps.PerformanceConfig',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 允许跨域请求配置
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # 允许跨域请求配置
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'performance_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'performance_management.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'performance_test',  # 数据库名字(需要先创建)
        'USER': 'root',  # 登录用户名
        'PASSWORD': 'lp990324',  # 密码
        'HOST': 'lvpeng990324.cn',  # 数据库IP地址,留空默认为localhost
        'PORT': '5432',  # 端口
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# 定义未登录要重定向的登录链接
LOGIN_URL = '/user_login/'

# 定义备份目录
BACKUP_DIR = os.path.join(BASE_DIR, 'backups')

# 发送邮件配置信息
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = 'lvpeng990324@163.com'  # 填写你的邮件地址
EMAIL_HOST_PASSWORD = 'lp990324'  # 密码
EMAIL_PORT = 25
EMAIL_USE_TLS = True

# 发送短信配置信息
# 接口链接
SMSAPI = "http://api.smsbao.com/"
# 短信平台账号
SMSUSER = 'lvpeng990324'
# 短信平台密码
SMSPASSWORD = 'lp990324'

# 微信登录配置信息
# 微信开发平台下网站应用的appid
APPID = "wxfe899b3596d5c097"
# 微信开发平台下网站应用的appsecret
APPSECRET = '8720a9324fbe5c5d8a0b1b3730b310a1'
# 微信开发平台下网站应用的回调域
REDIRECT_URL = 'http://debug.lvpeng990324.cn'

# 服务域名
# 部署本系统的网址，用于开放接口拼接链接使用
# 就是本系统首页的网址，最后不要加/
SITE_URL = 'demo.lvpeng990324.cn'
