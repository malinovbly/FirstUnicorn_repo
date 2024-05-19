from django.shortcuts import render
from vacancies.models import Vacancy


def vacancies(request):
    order_by = request.GET.get('order_by', None)
    vacancies = Vacancy.objects.all()

    if order_by and order_by != "default":
        vacancies = vacancies.order_by(order_by)

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
