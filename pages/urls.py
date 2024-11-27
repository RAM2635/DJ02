from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('third/', views.news_list, name='news_list'),  # Страница с новостями
    path('second/', views.second, name='second'),  # Вторая страница
    path('contacts/', views.contacts, name='contacts'),  # Контакты
]
