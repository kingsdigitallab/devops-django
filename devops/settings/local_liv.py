from .base import *  # noqa

INTERNAL_IPS = INTERNAL_IPS + ['']
ALLOWED_HOSTS = ['']

DATABASES = {
    'default': {
        'ENGINE': db_engine,
        'NAME': 'app_devops_liv',
        'USER': 'app_devops',
        'PASSWORD': '',
        'HOST': ''
    },
}

SECRET_KEY = ''
