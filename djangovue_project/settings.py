"""
Django settings for djangovue_project project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vtp&i1q!0^3tiq#b4nfhfb)rb1alfr4kdi@s(0w)!$==ju*-*g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['localhost:8000']
# Invalid HTTP_HOST header: 'localhost:8000'. You may need to add 'localhost' to ALLOWED_HOSTS.
ALLOWED_HOSTS = ['localhost'] # still doesn't work

# Application definition

INSTALLED_APPS = [
    # Installed by Django
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # https://github.com/pennersr/django-allauth/issues/57
    'django.contrib.sites',
    'django.contrib.staticfiles',

    # Third-party apps
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'debug_toolbar',

    # Local Apps
    'games.apps.GamesConfig',
    'users.apps.UsersConfig',
]

SITE_ID = 1 # django-allauth
# SITE_ID = 2 https://www.youtube.com/watch?v=56w8p0goIfs  ~11:00

#ACCOUNT_EMAIL_REQUIRED = True  See AUTHENTICATION SETTINGS

CRISPY_TEMPLATE_PACK = 'bootstrap4' # django-crispy-forms

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangovue_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        #'DIRS': [os.path.join(BASE_DIR, "templates")],  Windows os?
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangovue_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
"""

# also in local_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'play2learn',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': 5432
    }
}


# EMAIL
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
DEFAULT_FROM_EMAIL = 'bgroveben@gmail.com'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, even w/o `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth`-specific auth methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
#############################################################################
# AUTHENTICATION SETTINGS
# The AUTH_USER_MODEL setting sets the model used to represent a User in the
# project. It defaults to 'auth.User'. This code overrides that default to
# set it to the CustomUser class.
AUTH_USER_MODEL = 'users.CustomUser'
# AUTH_USER_MODEL = 'auth.User'
#LOGIN_URL = 'account_login'
LOGIN_URL = reverse_lazy('account:login')
# LOGIN_REDIRECT_URL = '/'
# LOGIN_REDIRECT_URL = 'pages:homepage'
LOGIN_REDIRECT_URL = 'games:homepage'

#LOGOUT_REDIRECT_URL = reverse_lazy('account:logout')
# ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login' # Default: '/'
# LOGIN_REDIRECT_URL = 'account_login'
# LOGIN_REDIRECT_URL = 'account_login'
# --> 127.0.0.1 redirected you too many times.

# https://stackoverflow.com/a/49656032/4806473

# django-allauth settings
ACCOUNT_AUTHENTICATION_METHOD = 'email' # Default: 'username'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1 # Default: 3
ACCOUNT_EMAIL_REQUIRED = True # Default: False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' # Default: 'optional'
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5 # Default: 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300 # Default 300
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login' # Default: '/'
#LOGOUT_REDIRECT_URL = reverse_lazy('account:logout')
ACCOUNT_LOGIN_REDIRECT_URL = reverse_lazy('games:homepage')
ACCOUNT_USERNAME_REQUIRED = True # Default: True


#ACCOUNT_CONFIRM_EMAIL_ON_GET = True


## allauth.account.forms
ACCOUNT_FORMS = {
    # Used to override forms, for example: {'login': 'myapp.forms.LoginForm'}
    'login': 'allauth.account.forms.LoginForm',
    'signup': 'allauth.account.forms.SignupForm',
    #'signup': 'allauth.account.forms.CustomSignupForm',
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'allauth.account.forms.ChangePasswordForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
    #'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
}
#############################################################################

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
      BASE_DIR / 'static',
  ]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.AllowAllUsersModelBackend', )

# BOTTOM OF settings.py
if os.environ.get('ENVIRONMENT') != 'production':
    from .local_settings import *
# DON'T PUT ANYTHING BELOW THIS
