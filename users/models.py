from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    patronymic = models.CharField(max_length=150, blank=True, null=True, verbose_name='Отчество')
    city = models.CharField(max_length=150, default='Екатеринбург', verbose_name='Город')
    profession = models.CharField(max_length=150, blank=True, null=True, verbose_name='Профессия')
    work_experience = models.CharField(max_length=150, blank=True, null=True, verbose_name='Стаж')
    self_info = models.TextField(max_length=350, blank=True, null=True, verbose_name='О себе')

    
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return self.username
