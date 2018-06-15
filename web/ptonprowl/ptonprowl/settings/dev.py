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
        'NAME': 'prowl_db',
        'USER': 'root',
        'PASSWORD': keys.ROOT_PW,
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
