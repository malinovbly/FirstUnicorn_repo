from django.shortcuts import render
from vacancies.models import Vacancy


def vacancies(request):
    vacancies = Vacancy.objects.all()

    context = {
        'title': 'FirstUnicorn | Вакансии',
        'vacancies': vacancies,
    }

    return render(request, 'vacancies/vacancies.html', context)


def vacancy(request, vacancy_slug):
    vacancy = Vacancy.objects.get(slug=vacancy_slug)

    context = {
        'title': vacancy.name,
        'vacancy': vacancy,
    }

    return render(request, 'vacancies/vacancy.html', context)
