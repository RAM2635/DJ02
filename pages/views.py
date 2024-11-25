from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def second(request):
    return render(request, 'pages/second.html')

def third(request):
    return render(request, 'pages/third.html')

def contacts(request):
    return render(request, 'pages/contacts.html')
