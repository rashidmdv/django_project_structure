from .settings import *

DEBUG = False
SHELL_PLUS = "ipython"

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:5173'
]




