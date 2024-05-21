from django.http import HttpResponse
from django.shortcuts import render

from vacancies.models import Vacancy


def index(request):
    popular_vacancies = Vacancy.objects.filter(id__lt=4)

    context = {
        'title': 'FirstUnicorn',
        'popular_vacancies': popular_vacancies,
    }
        
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'FirstUnicorn | О нас'
    }

    return render(request, 'main/about.html', context)
