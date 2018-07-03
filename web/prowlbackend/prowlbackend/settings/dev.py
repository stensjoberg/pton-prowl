# imports base settings
from .base import *

#
# Custom development settings
#

DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prowlbackend_db',
        'USER': 'root',
        'PASSWORD': keys.ROOT_PW,
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# allows cross-site HTTP requests from dev React IP-port config
CORS_ORIGIN_WHITELIST = [
    'localhost:3000'
]

# allowed ips on which dev server can be hosted
ALLOWED_HOSTS = [
    '0.0.0.0',
    'localhost'
]

# Debug
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        #'rest_framework-permissions.IsAuthenticated',
    ),
}
