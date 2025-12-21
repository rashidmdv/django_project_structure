import os
from . import BASE_DIR


DATABASE = os.getenv('DATABASE', 'sqlite')

if DATABASE == "mysql":
    DATABASES_CONFIG = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('DB_DATABASE', 'django_inventory'),
            'USER': os.getenv('DB_USERNAME', 'root'),
            'PASSWORD': os.getenv('DB_PASSWORD', ''), 
            'HOST': os.getenv('DB_HOST', '127.0.0.1'),
            'PORT': os.getenv('DB_PORT', '3306'),
        }
    }
elif DATABASE == "postgresql":
    DATABASES_CONFIG = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_DATABASE', 'django_inventory'),
            'USER': os.getenv('DB_USERNAME', 'root'),
            'PASSWORD': os.getenv('DB_PASSWORD', ''),
            'HOST': os.getenv('DB_HOST', '127.0.0.1'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }
else:
    DATABASES_CONFIG = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }