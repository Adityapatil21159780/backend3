"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
import psycopg2
from corsheaders.middleware import CorsMiddleware

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x(5dx3mmj4*37yh956zl74#t=wvbuib)!87s7)lg&v!9h6sf)a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'https://api.ehappyperformer.com','http://api.ehappyperformer.com','127.0.0.1']
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    "https://api.ehappyperformer.com",
    "https://www.ehappyperformer.com",
]
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    "https://api.ehappyperformer.com",
    "http://api.ehappyperformer.com",
]
CORS_ORIGIN_WHITELIST = [
    'http://localhost:5173',
    "https://api.ehappyperformer.com",
    "http://api.ehappyperformer.com",
    "https://www.ehappyperformer.com",  # Adjust this to match your frontend URL
]

SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Store sessions in the database
SESSION_COOKIE_NAME = 'sessionid'  # Default is 'sessionid', can be changed
SESSION_COOKIE_HTTPONLY = True  # Same as 'httpOnly: true' in Express
SESSION_COOKIE_SECURE = False  # Set to True in production
SESSION_SAVE_EVERY_REQUEST = False  # Same as 'resave: false' in Express
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Session will not expire when the browser closes
SESSION_COOKIE_SAMESITE = 'Lax'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',

    'corsheaders',
    'rest_framework',
    'happyPerformerBackend',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
<<<<<<< HEAD
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'dbms@123',
=======
        'NAME': 'login1',
        'USER': 'postgres',
        'PASSWORD': 'Adi@2115',
>>>>>>> 174a167 (backend1)
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# manually added
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760  # 10 MB

LOGIN_URL = '/login/'

# uncomment these for email service
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'dummyyWork122@gmail.com'
EMAIL_HOST_PASSWORD = 'ndkv ujlh tpfm lgrd'

# TO get the password: Go to your google account-> Manage google account-> Search "App passwords (Security)"-> Create password.


#added
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

# settings.py
EMAIL_SEPARATOR = ','
