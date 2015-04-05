"""
Django settings for fdregister project.
"""

import os
from conf import site_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = site_settings.SECRET_KEY
DEBUG = site_settings.DEBUG
TEMPLATE_DEBUG = site_settings.TEMPLATE_DEBUG
ALLOWED_HOSTS = site_settings.ALLOWED_HOSTS
DATABASES = site_settings.DATABASES

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'www',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fdregister.urls'
WSGI_APPLICATION = 'fdregister.wsgi.application'
LANGUAGE_CODE = site_settings.LANGUAGE_CODE
TIME_ZONE = site_settings.TIME_ZONE
USE_I18N = site_settings.USE_I18N
USE_L10N = site_settings.USE_L10N
USE_TZ = site_settings.USE_TZ
STATIC_URL = site_settings.STATIC_URL

# fdregister specific config

CAL_MONTHS = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}

