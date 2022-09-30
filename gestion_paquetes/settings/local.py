from .common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'paquetes',
        'USER': 'postgres',
        'PASSWORD': 'Tascon1234W',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}