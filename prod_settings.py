import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False

DB = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': 'ec2-3-224-184-9.compute-1.amazonaws.com',
            'PORT': '5432',
            'NAME': 'dbb02pjruujbas',
            'USER': 'zakxbzcmzapjse',
            'PASSWORD': os.getenv('DB_PASSWORD'),
        }
    }

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
