"""
Django settings for metaespacio project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '57#f7u+v@yh*vwv^ox#%*wgx6c@_a*%8#)0@1f6#dt=oar4u$f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.getuid() >= 1000)
TEMPLATE_DEBUG = DEBUG


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'crispy_forms',
    'common',
    'registro',
    'espacios',
    'pages',
    'captcha',
    'taquilla',
    'encuestas',
    # 'bibliotheca',  # necesita actualizar a 1.8
    # 'tastypie',  # necesita actualizar a 1.8
    'django.contrib.admin',  # al final por un override de templates
    'cuotas',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = \
    global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
        'common.context_processor.site',
    )

ROOT_URLCONF = 'metaespacio.urls'

WSGI_APPLICATION = 'metaespacio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

TEMPLATE_LOADERS = ('django.template.loaders.app_directories.Loader', )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

from .settings_local import *

if DEBUG:
    # static en desarrollo en carpeta del proyecto
    STATIC_ROOT = os.path.join(BASE_DIR, '.static')
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    # errores por consola
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    # en desarrollo no se usa
    ALLOWED_HOSTS = []
    INSTALLED_APPS += ('debug_toolbar', )
else:
    # FIXME Esto revisarlo porque tampoco lo estamos poniendo aqui exactamente
    STATIC_ROOT = '/var/www/metaespacio/static/'
    MEDIA_ROOT = '/opt/metaespacio/media/'
    # Envia correos bien
    ADMINS = (("Root", "changeme@andensinlimite.org"), )
    # en preproduccion o produccion si se usa
    ALLOWED_HOSTS = ['*']

MEDIA_URL = "/media/"
STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = "/"
CRISPY_TEMPLATE_PACK = "bootstrap3"
