"""
Django settings for Restaurant project.

Generated by 'django-admin startproject' using Django 4.1.6.

Для отримання додаткової інформації про цей файл див.
https://docs.djangoproject.com/en/4.1/topics/settings/

Повний список налаштувань та їхні значення дивіться у розділі
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Побудуйте шляхи всередині проєкту таким чином: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Налаштування швидкого запуску розробки - непридатні для виробництва
# Див. https://docs.djangoproject.com/en/4.1/howto/deployment/checklist

# ПОПЕРЕДЖЕННЯ БЕЗПЕКИ: зберігайте секретний ключ, який використовується у виробництві, в таємниці!
SECRET_KEY = 'SECRET_KEY'

# ПОПЕРЕДЖЕННЯ З БЕЗПЕКИ: не запускайте з увімкненим налагодженням у продакшені!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition (Визначення програми)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    'account.apps.AccountConfig',
    'main_page.apps.MainPageConfig',
    'manager.apps.ManagerConfig'
    # 'cafe_menu.apps.CafeMenuConfig',
    # 'cafe_events.apps.CafeEventsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Restaurant.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Restaurant.wsgi.application'

# Database (База даних)
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation (Перевірка пароля)
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

# Internationalization (Інтернаціоналізація)
# https://docs.djangoproject.com/en/4.1/topics/i18n

LANGUAGE_CODE = 'uk-ua'
# LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images) (Статичні файли (CSS, JavaScript, зображення))
# https://docs.djangoproject.com/en/4.1/howto/static-files

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Default primary key field type (Тип поля первинного ключа за замовчуванням)
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
