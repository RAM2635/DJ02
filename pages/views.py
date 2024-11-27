from django.shortcuts import render
from .models import News

def home(request):
    news = News.objects.all().order_by('-published_date')  # Все новости по дате
    return render(request, 'pages/home.html', {'news': news})

def news_list(request):
    news = News.objects.all().order_by('-published_date')  # Все новости по дате
    return render(request, 'pages/third.html', {'news': news})

def second(request):
    return render(request, 'pages/second.html')

def third(request):
    return render(request, 'pages/third.html')

def contacts(request):
    return render(request, 'pages/contacts.html')
