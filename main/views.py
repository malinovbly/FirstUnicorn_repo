from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'FirstUnicorn',
        'popular_vacancies': [
            {
                'name': 'Профессиональные услуги токаря',
                'description': 'Предлагаю услуги профессионального токаря с многолетним опытом работы. Изготавливаю и ремонтирую детали различной сложности из металла и пластика по чертежам заказчика.',
                'price': 500.00,
                'author_link': 'author_link_here',
                'image': 'image_here',
            },
            {
                'name': 'Механообработка металлов и сплавов',
                'description': 'Профессиональная механообработка деталей любой сложности на современных станках. Обеспечим точность и качество обработки, строго соблюдаем сроки.',
                'price': 500.00,
                'author_link': 'author_link_here',
                'image': 'image_here',
            },
            {
                'name': 'Услуги квалифицированного слесаря',
                'description': 'Предлагаю услуги опытного слесаря по ремонту и обслуживанию оборудования. Быстро и качественно выполним слесарные работы любой сложности.',
                'price': 500.00,
                'author_link': 'author_link_here',
                'image': 'image_here',
            },
        ]
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

