# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
from mysite.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ub86iu+m2yw6fvsgl!@aw-7h*c==ihssentv=4ezehev90n6ep"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SITE_ID = 2
ALLOWED_HOSTS = ["domin2000.com", "www.domin2000.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
STARIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
