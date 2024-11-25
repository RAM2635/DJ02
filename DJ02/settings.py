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
        'ENGINE': 'django.db.backends.dummy',
    }
}

# Указываем путь к модулю маршрутов
ROOT_URLCONF = 'DJ02.urls'

# Список установленных приложений
INSTALLED_APPS = [
    'django.contrib.staticfiles',  # Для работы со статическими файлами
    'pages',  # Ваше приложение
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
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
            ],
        },
    },
]

# Настройка статических файлов
STATIC_URL = '/static/'
