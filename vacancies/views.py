from django.shortcuts import render


def vacancies(request):
    context = {
        'title': 'FirstUnicorn | Вакансии',
        'vacancies': [
            {
                'name': 'Производство втулок.',
                'description': 'Изготовление втулок на станке. Срок - 4 дня.',
                'price': '500.00',
            },
            {
                'name': 'Замена подшипника.',
                'description': 'Произведу замену старого подшипника в детали. Срок - 7 дней.',
                'price': '700.00',
            },
        ]
    }

    return render(request, 'vacancies/vacancies.html', context)


def vacancy(request):
    context = {
        'title': 'FirstUnicorn | {Название вакансии}'
    }

    return render(request, 'vacancies/vacancy.html', context)
