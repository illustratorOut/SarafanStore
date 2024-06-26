from django.contrib import admin

from cart.models import CartProduct


@admin.register(CartProduct)
class SubcategoryAdmin(admin.ModelAdmin):
    '''
    Фильтр по (автору и названию)
    Поиск по (названию)
    '''
    list_display = ('pk', 'user', 'product', 'quantity', 'release_date')
    list_filter = ('user', 'product',)
    search_fields = ('product',)
    list_display_links = ('product',)
