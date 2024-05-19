from django.shortcuts import render
from vacancies.models import Vacancy


def vacancies(request):
    context = {
        'title': 'FirstUnicorn | Вакансии',
        'vacancies': [
            {
                'name': 'Профессиональные услуги токаря',
                'description': 'Предлагаю услуги профессионального токаря с многолетним опытом работы. Изготавливаю и ремонтирую детали различной сложности из металла и пластика по чертежам заказчика.',
                'make_time': '2 дня',
                'price': 500.00,
                'author_link': 'author_link_here',
                'image': 'image_here',
            },
            {
                'name': 'Механообработка металлов и сплавов',
                'description': 'Профессиональная механообработка деталей любой сложности на современных станках. Обеспечим точность и качество обработки, строго соблюдаем сроки.',
                'make_time': '3 дня',
                'price': 500.00,
                'author_link': 'author_link_here',
                'image': 'image_here',
            },
            {
                'name': 'Услуги квалифицированного слесаря',
                'description': 'Предлагаю услуги опытного слесаря по ремонту и обслуживанию оборудования. Быстро и качественно выполним слесарные работы любой сложности.',
                'make_time': '4 дня',
                'price': 500.00,
                'author_link': 'author_link_here',
                'image': 'image_here',
            },
            {
                'name': 'Ремонт посадочного места в вале',
                'description': 'Отремонтирую посадочное место в вале.',
                'make_time': '3 дня',
                'price': 500.00,
                'author_link': 'author_link_here',
                'image': 'image_here',
            },
            {
                'name': 'Замена подшипника в детали',
                'description': 'Заменяю подшипники в различных деталях.',
                'make_time': '7 дней',
                'price': 500.00,
                'author_link': 'author_link_here',
                'image': 'image_here',
            },
            {
                'name': 'Изготовление втулок',
                'description': 'Изготавливаю втулки на собственном станке.',
                'make_time': '4 дня',
                'price': 500.00,
                'author_link': 'author_link_here',
                'image': 'image_here',
            },
            {
                'name': 'Вытачивание заготовок на станке',
                'description': 'Могу выточить разнообразные заготовки по заказу.',
                'make_time': '14 дней',
                'price': 500.00,
                'author_link': 'author_link_here',
                'image': 'image_here',
            },
            {
                'name': 'Обработка деталей',
                'description': 'Обработаю ваши детали: отполирую, подточу и тп.',
                'make_time': '5 дней',
                'price': 500.00,
                'author_link': 'author_link_here',
                'image': 'image_here',
            },
            {
                'name': 'Нанесение резьбы',
                'description': 'Сделаю первоклассную резьбу на ваших деталях.',
                'make_time': '2 дня',
                'price': 500.00,
                'author_link': 'author_link_here',
                'image': 'image_here',
            },
        ]
    }

    return render(request, 'vacancies/vacancies.html', context)


def vacancy(request):
    # vacancies = Vacancy.objects.all()

    context = {
        'title': 'FirstUnicorn | {Название вакансии}',
    }

    return render(request, 'vacancies/vacancy.html', context)
