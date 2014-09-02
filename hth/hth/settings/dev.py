from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += (
    'debug_toolbar.apps.DebugToolbarConfig',
    'core.tests',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}
