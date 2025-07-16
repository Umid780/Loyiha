INSTALLED_APPS = [
    ...,
    'market',
    'rest_framework',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'market/static']

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
