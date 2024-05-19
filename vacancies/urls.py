from django.urls import path
from vacancies import views

app_name = 'vacancies'

urlpatterns = [
    path('', views.vacancies, name='index'),
    path('vacancy/<slug:vacancy_slug>/', views.vacancy, name='vacancy'),
]