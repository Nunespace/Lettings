from dotenv import load_dotenv
import os
import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


# Initialise environment variables
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
load_dotenv()

# voir https://devcenter.heroku.com/articles/django-app-configuration
IS_HEROKU = "DYNO" in os.environ


# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file to the root of the project
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
if not IS_HEROKU:
    DEBUG = True

# Generally avoid wildcards(*). However since Heroku router provides
# hostname validation it is ok
if IS_HEROKU:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "oc_lettings_site.apps.OCLettingsSiteConfig",
    # to use the Django admin feature:
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # Use WhiteNoise's runserver implementation instead of the Django default,
    # for dev-prod parity.
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "lettings",
    "profiles",
]
# WhiteNoise permet à une application web de servir ses propres
# fichiers statiques, ce qui en fait une unité autonome
# qui peut être déployée n'importe où
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # Django ne prend pas en charge le chargement des fichiers statiques en
    # production, le paquet WhiteNoise est utilisé ici à la place.
    # L’intergiciel WhiteNoise doit être listé après le protocole
    # SecurityMiddleware de Django afin que les redirections de sécurité
    # soient toujours effectuées. Voir : https://whitenoise.readthedocs.io
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "oc_lettings_site.urls"

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

WSGI_APPLICATION = "oc_lettings_site.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "oc-lettings-site.sqlite3"),
    }
}


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
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# voir https://docs.djangoproject.com/fr/5.0/howto/deployment/checklist/
if IS_HEROKU:
    # HSTS = Sécurité de transport HTTP stricte
    # pour refuser les connexions au nom de domaine si la connexion n’est pas sécurisée
    # voir https://docs.djangoproject.com/fr/5.0/ref/middleware/#http-strict-transport-security)
    #SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    #SECURE_HSTS_SECONDS = 3600
    #SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    #  SecurityMiddleware redirige toutes les requêtes non HTTPS vers HTTPS:
    SECURE_SSL_REDIRECT = True
    # voir https://docs.djangoproject.com/fr/5.0/howto/deployment/checklist/
    # pour éviter de transmettre le cookie CSRF accidentellement par HTTP:
    CSRF_COOKIE_SECURE = True
    # pour éviter de transmettre le cookie de session accidentellement par HTTP:
    SESSION_COOKIE_SECURE = True

try:
    sentry_sdk.init(
        dsn=os.environ["DSN"],
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
        # enable_tracing=True,
        debug=False,
        # environment="development",
        integrations=[DjangoIntegration()],
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
    )
except KeyError:
    print(
        "Sentry isn't running, because no 'SENTRY_DSN' was found in env variables."
    )
