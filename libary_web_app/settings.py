from pathlib import Path
from environs import Env
# import ldap
# from django_auth_ldap.config import LDAPSearch
import logging
import ssl

logger = logging.getLogger("django_auth_ldap")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANDGO_SECRET_KEY")
# DB_NAME = env('DB_NAME')
# DB_USERNAME = env('DB_USERNAME')
# DB_PASSWORD = env('BD_PASSWORD')
# DB_HOST = env('DB_HOST')
# DB_PORT =env('PORT')
LDAP_SERVER = env("LDAP_SERVER")
LDAP_SEARCH_BASE = env("ldap_search_base")
AUTH_LDAP_BIND_PASSWORD = env("LDAP_BIND_PASSWORD")
LDAP_BIND_DN = env("LDAP_BIND_DN")
DOMAIN = env("DOMAIN")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "library_app",
    "accounts",
    "crispy_forms",
    "crispy_bootstrap5",
    "django_python3_ldap",
]

LOGIN_REDIRECT_URL = "home"
AUTH_USER_MODEL = "accounts.CustomUser"
AUTHENTICATION_BACKENDS = [
    # "django_auth_ldap.backend.LDAPBackend",
    # "django_python3_ldap.auth.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "libary_web_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "libary_web_app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    # "equip": {
    #     "ENGINE": "mssql",
    #     "NAME": DB_NAME,
    #     "USER": DB_USERNAME,
    #     "PASSWORD": DB_PASSWORD,
    #     "HOST": DB_HOST,
    #     "PORT": DB_PORT,
    #     "OPTIONS": {"driver": "SQL Server Native Client 11.0"},
    # },
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

# LDAP configuration


LDAP_AUTH_USE_TLS = True
LDAP_AUTH_TLS_VERSION = ssl.PROTOCOL_TLSv1_2
LDAP_AUTH_TLS_CIPHERS = "ALL"

LDAP_AUTH_URL = LDAP_SERVER
LDAP_AUTH_SEARCH_BASE = LDAP_SEARCH_BASE
# LDAP_AUTH_OBJECT_CLASS = "inetOrgPerson"
LDAP_AUTH_FORMAT_USERNAME = "django_python3_ldap.utils.format_username_active_directory"

LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN = DOMAIN
LDAP_AUTH_FORMAT_USERNAME = (
    "django_python3_ldap.utils.format_username_active_directory_principal"
)

LDAP_AUTH_USER_FIELDS = {
    "username": "sAMAccountName",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}

LDAP_AUTH_OBJECT_CLASS = "user"
# LDAP_AUTH_CLEAN_USER_DATA = "django_python3_ldap.utils.clean_user_data"
LDAP_AUTH_CONNECTION_USERNAME = None
LDAP_AUTH_CONNECTION_PASSWORD = None

LDAP_AUTH_USER_LOOKUP_FIELDS = ("username",)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django_python3_ldap": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },
}


# django_ldap_settings

AUTH_LDAP_SERVER_URI = LDAP_SERVER

AUTH_LDAP_PERMIT_EMPTY_PASSWORD = True
AUTH_LDAP_BIND_DN = LDAP_BIND_DN
AUTH_LDAP_BIND_PASSWORD = AUTH_LDAP_BIND_PASSWORD
# AUTH_LDAP_USER_SEARCH = LDAPSearch(
#     , ldap.SCOPE_SUBTREE, "(SamAccountName=%(user)s)"
# )
# AUTH_LDAP_USER_DN_TEMPLATE = "SamAccountName=%(user)s,ou=St George's,DC=net,DC=stgeorges,DC=nhs,DC=uk"

# AUTH_LDAP_USER_SEARCH = LDAPSearch(
#     "OU=St George's,DC=net,DC=stgeorges,DC=nhs,DC=uk",
#     ldap.SCOPE_SUBTREE,
#     "(sAMAccountName=%(user)s)",
# )

# # You can map user attributes to Django attributes as so
# AUTH_LDAP_USER_ATTR_MAP = {
#     "first_name": "givenName",
#     "last_name": "sn",
#     "email": "mail",
# }
