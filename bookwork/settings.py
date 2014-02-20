"""
Django settings for bookwork project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
import random
from django.conf import global_settings

# Load Environment variables from .env file in the Root of the checkout

try:
    HOSTNAME = socket.gethostname()
except:
    HOSTNAME = '127.0.0.1:5000'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login-form/'
LOGIN_ERROR_URL = '/login-error/'

FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID','218166651721097')
FACEBOOK_API_SECRET = '20986a4550124333666539356d682d27'

LINKEDIN_CONSUMER_KEY = '75kgs7tme1ngdg'
LINKEDIN_CONSUMER_SECRET = 'IBSz1WygEeXXUik1'
LINKEDIN_SCOPE = ['r_basicprofile', 'r_emailaddress']
LINKEDIN_EXTRA_FIELD_SELECTORS = ['email-address']
LINKEDIN_EXTRA_DATA = [('id', 'id'),
                       ('first-name', 'first_name'),
                       ('last-name', 'last_name'),
                       ('email-address', 'email_address')]

SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

EMAIL_HOST = os.environ.get('EMAIL_HOST', 'bookwork.co')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', '"Bookwork!" <iamthekeymaster@bookwork.co>')

EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = os.environ.get('MAILGUN_ACCESS_KEY', 'key-4cfari9mza2gsi9cfhioird0qjgj-0o8')
MAILGUN_SERVER_NAME = os.environ.get('MAILGUN_SERVER_NAME', 'sandbox2391.mailgun.org')

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + ('django.core.context_processors.request',)

AUTHENTICATION_BACKENDS = global_settings.AUTHENTICATION_BACKENDS + ('social_auth.backends.facebook.FacebookBackend','social_auth.backends.contrib.linkedin.LinkedinBackend',)

if not os.environ.get('DATABASE_URL', False):
    os.environ['DATABASE_URL'] = 'postgres://bookwork:bookwork@localhost:5432/bookwork'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'q$==u(qg2hurhgeywgigprszv3o1ulw@9n6(nz=7dxm%22!1s$')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
#   'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'homepage',
    'registration',
    'splashpage',
    'student',
    'select2',
    'south',
    'social_auth',
)

ACCOUNT_ACTIVATION_DAYS = 7

SITE_ID = 1;

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

if os.environ.get('FORCE_SSL', False):
    MIDDLEWARE_CLASSES = ('sslify.middleware.SSLifyMiddleware', ) + MIDDLEWARE_CLASSES


ROOT_URLCONF = 'bookwork.urls'

WSGI_APPLICATION = 'bookwork.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

try:
    from local_settings import *
except ImportError:
    pass
