from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'FirstUnicorn'
    }
        
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'FirstUnicorn | О нас'
    }

    return render(request, 'main/about.html', context)


def profile(request):
    context = {
        'title': 'FirstUnicorn | Профиль'
    }

    return render(request, 'main/profile.html', context)

