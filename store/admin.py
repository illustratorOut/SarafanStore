from django.contrib import admin

from store.models import Category, Subcategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''
    Фильтр по (автору и названию)
    Поиск по (названию)
    '''
    list_display = ('pk', 'title', 'image_tag', 'release_date', 'author')
    list_filter = ('title', 'author',)
    search_fields = ('title',)
    list_display_links = ('title',)


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


