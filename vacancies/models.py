from django.db import models
from users.models import User

class Vacancy(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(max_length=300, blank=True, null=True, verbose_name='Описание')
    make_time = models.CharField(max_length=100, blank=True, verbose_name='Время работы')
    image = models.ImageField(upload_to='vacancies_images', blank=True, null=True, verbose_name='Фото')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Стоимость')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default=1)


    class Meta:
        db_table = 'vacancy'
        verbose_name = 'Вакансию'
        verbose_name_plural = 'Вакансии'


    def __str__(self):
        return self.name
