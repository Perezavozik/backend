import os
from pathlib import Path

from django.conf.locale import LANG_INFO

LANG_INFO['lez'] = {
    'bidi': False,           # не RTL
    'code': 'lez',           # именно этот код
    'name': 'Lezgin',        # имя по-английски
    'name_local': 'Лезгинский',  # имя на самом языке (опционально)
}

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
MEDIA_URL = f"{BASE_URL}/media/"
STATIC_URL = '/static/'
MEDIA_ROOT  = "/app/media"
STATIC_ROOT = '/app/static'


BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'jazzmin',
    "drf_yasg",
    'parler',
    "solo",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_cleanup.apps.CleanupConfig",
    'rest_framework',
    "django_prometheus",
    "corsheaders",
    'django_ckeditor_5',
    'content_list.congresses',
    "detail_pages_components.events.apps.EventsConfig",
    "detail_pages_components.awards.apps.AwardsConfig",
    "detail_pages_components.society.apps.SocietyConfig",
    "detail_pages_components.history.apps.HistoryConfig",
    "detail_pages_components.culture.apps.CultureConfig",
    "detail_pages_components.language.apps.LanguageConfig",
    "detail_pages_components.news_on_main.apps.NewsOnMainConfig",
    "detail_pages_components.our_projects.apps.OurProjectsConfig",
    "detail_pages_components.awards_candidate.apps.AwardsCandidateConfig",
    'media_library',
    'documents',
    "contacts",
    "reports",
    "about_us",
    "feedback_form",
    "telegram_feed",
    "search",
]

MIDDLEWARE = [
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]



LANGUAGES = [
    ('ru', 'Русский'),
    ('en', 'Лезгинский'),
]

PARLER_LANGUAGES = {
    None: (
        {'code': 'ru'},
        {'code': 'en'},
    ),
    'default': {
        'fallbacks': ['ru'],
        'hide_untranslated': False,
    }
}
PARLER_DEFAULT_LANGUAGE_CODE = 'ru'
ROOT_URLCONF = "config.urls"
LANGUAGE_CODE = "ru"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.i18n",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

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

LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CKEDITOR_UPLOAD_PATH = os.getenv('CKEDITOR_UPLOAD_PATH')

CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading", "|",
            "bold", "italic", "underline", "link", "|",
            "bulletedList", "numberedList", "|",
            "imageUpload", "mediaEmbed", "insertTable", "|",
            "undo", "redo"
        ],
        "language": "ru",
    }
}



JAZZMIN_SETTINGS = {
    "site_title": "Lezgian Admin",
    "site_header": "Lezgian Website Admin",
    "site_brand": "Lezgian",
    "welcome_sign": "Добро пожаловать!",
    "copyright": "Lezgian Development",
    "search_model": ["auth.User", "yourapp.YourModel"],
    "custom_css": "css/admin_custom.css",
    # Темы
    "theme": "cyborg",  # 👈 тёмная тема (или "flatly", "darkly", "lux" и др.)

    # Sidebar
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        # Добавь иконки для своих моделей
    },
}

JAZZMIN_SETTINGS["show_ui_builder"] = True
