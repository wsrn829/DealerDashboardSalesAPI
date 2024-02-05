"""
Django settings for sales_project project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from dotenv import load_dotenv

load_dotenv()


import os
import dj_database_url
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-=0#lozw6m8fg901fvz9(b-$@y*_3)v9tgbo9x2se(ezga0)(mj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


SECRET_KEY = config('SECRET_KEY')
DATABASE_URL = config('DATABASE_URL')


INSTALLED_APPS = [
    'corsheaders',
    'sales_rest.apps.SalesRestConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ALLOWED_HOSTS = [
    "*",
]

CSRF_TRUSTED_ORIGINS = [
    "https://dealerdashboard.netlify.app",
    "http://localhost:3000",
]


CORS_ALLOW_ALL_ORIGINS = True


CORS_ALLOW_CREDENTIALS = True


    # "dealer-dashboard-8d7b3aea3ae7.herokuapp.com",
    # "dealerdashboardserviceapi-db6bf25312d7.herokuapp.com",
    # "dealerdashboardsalesapi-f1c2cc0024f6.herokuapp.com",
    # "localhost",
    # "sales-api",
    # "project-beta-inventory-api-1",
    # "sales-api",


# CSRF_TRUSTED_ORIGINS = [
#     "https://dealerdashboard.netlify.app",
#     "https://dealer-dashboard-8d7b3aea3ae7.herokuapp.com",
#     "https://dealerdashboardserviceapi-db6bf25312d7.herokuapp.com",
#     "https://dealerdashboardsalesapi-f1c2cc0024f6.herokuapp.com",
#     "http://localhost:3000",
#     "http://localhost:8000",
#     "http://localhost:8080",
#     "http://localhost:8090",
# ]

# CORS_ALLOWED_ORIGINS = [
#     "http://*",
#     "https://*",
#     "https://dealerdashboard.netlify.app",
#     "https://dealer-dashboard-8d7b3aea3ae7.herokuapp.com",
#     "https://dealerdashboardserviceapi-db6bf25312d7.herokuapp.com",
#     "https://dealerdashboardsalesapi-f1c2cc0024f6.herokuapp.com",
# ]


# CORS_ALLOWED_ORIGINS = [
#     "http://*",
#     "https://*",
#     "https://dealerdashboard.netlify.app",
#     "https://dealer-dashboard-8d7b3aea3ae7.herokuapp.com",
#     "https://dealerdashboardserviceapi-db6bf25312d7.herokuapp.com",
#     "https://dealerdashboardsalesapi-f1c2cc0024f6.herokuapp.com",
# ]


DJWTO_MODE = "TWO-COOKIES"
DJWTO_ACCESS_TOKEN_LIFETIME = None

ROOT_URLCONF = 'sales_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'sales_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

from datetime import timedelta

CELERY_BEAT_SCHEDULE = {
    'poll-every-60-seconds': {
        'task': 'poll.poller.poll',
        'schedule': timedelta(seconds=60),
    },
}
