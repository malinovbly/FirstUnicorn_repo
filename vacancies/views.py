from django.shortcuts import get_list_or_404, render
from vacancies.models import Vacancy
from vacancies.utils import q_search


def vacancies(request):
    order_by = request.GET.get('order_by', None)
    vacancies = Vacancy.objects.all()
    query = request.GET.get('q', None)

    if query:
        vacancies = q_search(query)
        
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
