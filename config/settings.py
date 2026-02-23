"""
Django settings for Support System project.
"""

from pathlib import Path

# ===============================
# BASE DIRECTORY
# ===============================
BASE_DIR = Path(__file__).resolve().parent.parent


# ===============================
# SECURITY SETTINGS
# ===============================
SECRET_KEY = 'django-insecure-change-this-before-production'

DEBUG = True

ALLOWED_HOSTS = []


# ===============================
# INSTALLED APPS
# ===============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom apps
    'accounts',
    'tickets',
    'dashboard',
]


# ===============================
# MIDDLEWARE
# ===============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ===============================
# URL CONFIGURATION
# ===============================
ROOT_URLCONF = 'config.urls'


# ===============================
# TEMPLATES
# ===============================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # Global templates folder
        'DIRS': [BASE_DIR / 'templates'],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ===============================
# WSGI APPLICATION
# ===============================
WSGI_APPLICATION = 'config.wsgi.application'


# ===============================
# DATABASE (SQLite)
# ===============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ===============================
# PASSWORD VALIDATION
# ===============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ===============================
# INTERNATIONALIZATION
# ===============================
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True
USE_TZ = True


# ===============================
# STATIC FILES
# ===============================
STATIC_URL = 'static/'

# Custom static folder
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'