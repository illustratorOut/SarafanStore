from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''
    Модель пользователя
    Фильтр по роли пользователя
    '''
    list_display = ('pk', 'email', 'first_name', 'phone', 'is_active',)
    list_filter = ('email',)
