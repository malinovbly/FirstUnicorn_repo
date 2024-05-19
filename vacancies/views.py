from django.shortcuts import render
from vacancies.models import Vacancy


def vacancies(request):
    vacancies = Vacancy.objects.all()

    context = {
        'title': 'FirstUnicorn | Вакансии',
        'vacancies': vacancies,
    }

    return render(request, 'vacancies/vacancies.html', context)


def vacancy(request):
    # vacancies = Vacancy.objects.all()

    context = {
        'title': 'FirstUnicorn | {Название вакансии}',
    }

    return render(request, 'vacancies/vacancy.html', context)
