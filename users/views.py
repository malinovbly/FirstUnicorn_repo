from django.shortcuts import render


def login(request):
    context = {
        'title': 'FirstUnicorn | Авторизация'
    }

    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'FirstUnicorn | Регистрация'
    }

    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'FirstUnicorn | Профиль'
    }

    return render(request, 'users/profile.html', context)


def logout(request):
    ...
