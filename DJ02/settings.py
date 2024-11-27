from decouple import config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ проекта
SECRET_KEY = config('SECRET_KEY', default='your-default-secret-key')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Настройка фиктивной базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Указываем путь к модулю маршрутов
ROOT_URLCONF = 'DJ02.urls'

# Список установленных приложений
INSTALLED_APPS = [
    'django.contrib.admin',         # Для админ-панели
    'django.contrib.auth',          # Для аутентификации
    'django.contrib.contenttypes',  # Для работы с типами контента
    'django.contrib.sessions',      # Для работы с сессиями
    'django.contrib.messages',      # Для системы сообщений
    'django.contrib.staticfiles',   # Для работы со статическими файлами
    'pages',                        # Ваше приложение
]


# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Для сессий
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Для аутентификации
    'django.contrib.messages.middleware.MessageMiddleware',  # Для сообщений
]


# Настройка шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Путь к пользовательским шаблонам
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',  # Добавить это
                'django.contrib.messages.context_processors.messages',  # Добавить это
            ],
        },
    },
]


# Настройка статических файлов
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LANGUAGE_CODE = 'ru'
