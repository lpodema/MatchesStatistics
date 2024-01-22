from Backend.settings.dev import * # noqa
from pathlib import Path
from os.path import join


DEBUG = True

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

PROFILE_IMG = join(BASE_DIR, "/tests/profile_img/")
