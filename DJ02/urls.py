from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Админ-панель
    path('', include('pages.urls')),  # Маршруты приложения pages
]
