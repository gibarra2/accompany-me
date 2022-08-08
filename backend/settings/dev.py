from .common import *

DEBUG = True
SECRET_KEY = os.environ.get("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'accompany_me_development',
        'HOST': 'localhost', 
        'USER': 'root',
        'PASSWORD': os.environ.get("DB_PW"),
    }
}