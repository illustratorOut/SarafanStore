from django.contrib import admin

from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''
    Фильтр по (автору и названию)
    Поиск по (названию)
    '''
    list_display = ('pk', 'title', 'price', 'img', 'release_date', 'author')
    list_filter = ('title', 'author',)
    search_fields = ('title',)
    list_display_links = ('title',)
