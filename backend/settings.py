"""
Django settings for backend project.
"""

from pathlib import Path
import os

# -------------------------------------
# BASE DIRECTORY
# -------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# -------------------------------------
# SECURITY SETTINGS
# -------------------------------------
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "unsafe-secret-key")
DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = ["*"]


# -------------------------------------
# INSTALLED APPS
# -------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third party
    "rest_framework",
    "corsheaders",

    # Local
    "portfolio",
]


# -------------------------------------
# MIDDLEWARE
# -------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# -------------------------------------
# URL CONFIG
# -------------------------------------
ROOT_URLCONF = "backend.urls"


# -------------------------------------
# TEMPLATES
# -------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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


# -------------------------------------
# WSGI
# -------------------------------------
WSGI_APPLICATION = "backend.wsgi.application"


# -------------------------------------
# DATABASE
# -------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# -------------------------------------
# PASSWORD VALIDATION
# -------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# -------------------------------------
# INTERNATIONALIZATION
# -------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# -------------------------------------
# STATIC & MEDIA
# -------------------------------------
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# -------------------------------------
# CORS
# -------------------------------------
CORS_ALLOW_ALL_ORIGINS = True


# -------------------------------------
# EMAIL CONFIGURATION (GMAIL)
# -------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True


EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# -------------------------------------
# DEFAULT PRIMARY KEY
# -------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
