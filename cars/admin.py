from django.contrib import admin
from .models import *  # Из текущей папки из файла models импортируем всё


class UserAdmin(admin.ModelAdmin):
    # list_display = ['name', 'email']
    list_display = [field.name for field in User._meta.fields]
    #search_fields = ['name', 'email'] # ищем по имени и имейлу
    #list_filter = ['name']  # этот фильтр косаеться общего списка
    # exclude = ["email"]  # указываем то что не хотим показать на странице, єто могут біть личные данные и т.д.
    # fields = ["name"]     # указываем то что  хотим показать


class Meta:
    model = User


admin.site.register(User, UserAdmin)
