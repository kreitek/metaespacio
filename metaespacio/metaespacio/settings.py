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
PRODUCCION = False
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
    'oidc_provider',
    'crispy_forms',
    'common',
    'registro',
    'espacios',
    'pages',
    'taquilla',
    'encuestas',
    # 'bibliotheca',  # necesita actualizar a 1.8
    # 'tastypie',  # necesita actualizar a 1.8
    'django.contrib.admin',  # al final por un override de templates
    'cuotas',
    'graphos',
    'contabilidad',
    'adjuntos',
    'caronte',
    'rest',
    'rest_framework',
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

# SITE_ID = 1

TEMPLATE_LOADERS = ('django.template.loaders.app_directories.Loader', )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

# cosas custom
MEDIA_URL = "/media/"
STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = "/"
CRISPY_TEMPLATE_PACK = "bootstrap3"
SITE_URL = 'http://metaespacio.org'
LOGIN_URL = '/accounts/login'
OIDC_RSA_KEY_FOLDER = BASE_DIR
DEFAULT_FROM_EMAIL = 'cambiame@que.soy.util'

try:
    from .settings_local import *  # noqa
except ImportError:
    pass

if DEBUG:
    # static en desarrollo en carpeta del proyecto
    STATIC_ROOT = os.path.join(BASE_DIR, '.static')
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    # en desarrollo no se usa
    ALLOWED_HOSTS = []
    INSTALLED_APPS += ('debug_toolbar', )
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

if PRODUCCION:
    # FIXME Esto revisarlo porque tampoco lo estamos poniendo aqui exactamente
    STATIC_ROOT = '/var/www/metaespacio/static/'
    MEDIA_ROOT = '/opt/metaespacio/media/'
    # en preproduccion o produccion si se usa
    ALLOWED_HOSTS = ['*']
else:
    # errores por consola
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
