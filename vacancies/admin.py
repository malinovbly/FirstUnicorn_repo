from django.contrib import admin
from vacancies.models import Vacancy


# admin.site.register(Vacancy)

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
