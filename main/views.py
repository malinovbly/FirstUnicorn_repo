from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'FirstUnicorn',
        'content': 'Это главная'
    }
        
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'About Us',
        'content': 'Мы: я, он, он...'
    }

    return render(request, 'main/about.html', context)

