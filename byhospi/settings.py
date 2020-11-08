import os

import dj_database_url
from django.contrib.staticfiles import finders

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "#qk+*p#(me&lp9fm1dtq6_3yb&95gmk=(3!$bglmn_748dw5m7"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "django-byhospi.herokuapp.com"]

# Application definition

INSTALLED_APPS = [
    "djangobower",
    "client",
    "map",
    "hospital",
    "registration",
    "map.templatetags",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
ROOT_URLCONF = "byhospi.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "byhospi.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "production": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "d2o212jsq1k1cq",
        "USER": "ipryhmwjbrrkpl",
        "PASSWORD": "c95bd38e304c2763e1f567a005f6d3ee3decd0e73165e1670b209ef46a7d4686",
        "HOST": "ec2-52-6-143-153.compute-1.amazonaws.com",
        "PORT": "5432",
    },
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "1919",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    },
}
db_from_env = dj_database_url.config()
DATABASES["default"].update(db_from_env)
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


# settings/base.py
STATIC_ROOT = os.path.join(BASE_DIR, "staticfile")
STATIC_URL = "/static/"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATICFILES_FINDERS = [
    "djangobower.finders.BowerFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
BOWER_COMPONENTS_ROOT = "/home/zhenya/PycharmProjects/django/byhospi/"

BOWER_INSTALLED_APPS = (
    "jquery#3.5.0",
    "underscore",
)
