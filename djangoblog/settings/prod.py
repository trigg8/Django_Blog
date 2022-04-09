import django_on_heroku
from decouple import config

from djangoblog.settings.dev import ALLOWED_HOSTS


from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    ''
]