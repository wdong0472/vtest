# -*- coding: utf-8 -*-
"""
Django settings for share2i project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u&y23rlxh$uq_npi2$hath&!zm_%j=(ffykcr7g)=(+5y3ynm+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.share2i.com','120.79.76.70','share2i.com', 'wdong.site','localhost','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'suit',
    'django.contrib.sites',
    #'cms',
    #'menus',
    #'treebeard',
    #'djangocms_admin_style',
    #'sekizai',
    #'filer',
    #'easy_thumbnails',
    #'mptt',    
    # 'djangocms_text_ckeditor',
    # 'djangocms_link',
    # 'djangocms_file',
    # 'djangocms_picture',
    # 'djangocms_video',
    # 'djangocms_googlemap',
    # 'djangocms_snippet',
    # 'djangocms_style',    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'qrik_tools',
    'qrik_ui',
    'qrik_data',
    'qrik_auth',
    'qrik_demo',
    'qrik_test',
    'qrik_widgets',
    'wx',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # 'cms.middleware.user.CurrentUserMiddleware',
    # 'cms.middleware.page.CurrentPageMiddleware',
    # 'cms.middleware.toolbar.ToolbarMiddleware',
    # 'cms.middleware.language.LanguageCookieMiddleware',    
    # 'cms.middleware.utils.ApphookReloadMiddleware',
]

ROOT_URLCONF = 'share2i.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, '..', 'templates').replace('\\','/'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #'sekizai.context_processors.sekizai',
                #'cms.context_processors.cms_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'share2i.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


LANGUAGES = [
    ('en', 'English'),
    ('de', 'German'),
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'


# USE_I18N = True
# USE_L10N = True
# USE_TZ = True
#LANGUAGE_CODE = 'zh-hans'

LANGUAGE_CODE = 'en'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True
USE_L10N = False  
USE_TZ = False  
DATETIME_FORMAT = 'Y-m-d H:i:s'  
DATE_FORMAT = 'Y-m-d'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

# wdong@2017-06-28 added
# STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, "static"),
    # '/var/www/static/',
# )


STATICFILES_FINDERS = (
"django.contrib.staticfiles.finders.FileSystemFinder",
"django.contrib.staticfiles.finders.AppDirectoriesFinder"
)

#Session过期设置(只能二选一)
#1. 关闭浏览器则过期
SESSION_EXPIRE_AT_BROWSER_CLOSE=True
#2. 设置过期时间
#SESSION_EXPIRE_AT_BROWSER_CLOSE=False
#SESSION_SAVE_EVERY_REQUEST=True
#SESSION_COOKIE_AGE=1*60

try:
    from local_settings import *
except ImportError:
    pass

# # django-cms need
# SITE_ID = 1

# CMS_TEMPLATES = [
    # ('home.html', 'Home page template'),
# ]

# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# THUMBNAIL_HIGH_RESOLUTION = True

# THUMBNAIL_PROCESSORS = (
    # 'easy_thumbnails.processors.colorspace',
    # 'easy_thumbnails.processors.autocrop',
    # 'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    # 'easy_thumbnails.processors.filters'
# )

DATA_UPLOAD_MAX_NUMBER_FIELDS = 20240


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True #False   #是否使用TLS安全传输协议(用于在两个通信应用程序之间提供保密性和数据完整性。)
EMAIL_USE_SSL = False #True    #是否使用SSL加密，qq企业邮箱要求使用
EMAIL_HOST = 'smtp.263.net'   #发送邮件的邮箱 的 SMTP服务器，这里用了163邮箱
EMAIL_PORT = 25     #发件箱的SMTP服务器端口
EMAIL_HOST_USER = 'wangdong@kmopt.com'    #发送邮件的邮箱地址
EMAIL_HOST_PASSWORD = 'wdong@0522?'         #发送邮件的邮箱密码(这里使用的是授权码)
DEFAULT_FROM_EMAIL = 'wangdong@kmopt.com'
