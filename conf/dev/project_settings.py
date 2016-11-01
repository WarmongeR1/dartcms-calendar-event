# coding: utf-8
# Project and environment specific settings.

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APP_DOMAIN = 'example.com'
APP_URL = 'http://%s:8000' % APP_DOMAIN

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# TODO добавить issue в boilerplate на изменение дефолт базы на sqlite
