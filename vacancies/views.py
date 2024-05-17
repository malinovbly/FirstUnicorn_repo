from django.shortcuts import render


def vacancies(request):
    context = {
         'title': 'FirstUnicorn | Вакансии'
    }

    return render(request, 'vacancies/vacancies.html', context)


def vacancy(request):
    context = {
        'title': 'FirstUnicorn | {Название вакансии}'
    }

    return render(request, 'vacancies/vacancy.html', context)
