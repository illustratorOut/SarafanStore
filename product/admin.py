from django.contrib import admin
from django.utils.safestring import mark_safe

from product.models import Product, Category, Subcategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''
    Фильтр по (автору и названию)
    Поиск по (названию)
    '''
    list_display = ('pk', 'title', 'image_show', 'release_date', 'author')
    list_filter = ('title', 'author',)
    search_fields = ('title',)
    list_display_links = ('title',)

    def image_show(self, obj):
        if obj.img:
            return mark_safe("<img src='{}' width='100px'/>".format(obj.img.url))
        else:
            return 'No Image Found'

    image_show.short_description = 'Изображение'


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    '''
    Фильтр по (автору и названию)
    Поиск по (названию)
    '''
    list_display = ('pk', 'title', 'img', 'release_date', 'author')
    list_filter = ('title', 'author',)
    search_fields = ('title',)
    list_display_links = ('title',)


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
