from app_db.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'app',
        'USER': 'root',
        'PASSWORD': 'surajshah',
        'HOST': 'localhost',
        'PORT': '',
    }
}


