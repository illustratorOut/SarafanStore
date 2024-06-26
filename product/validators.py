from rest_framework.exceptions import ValidationError

from product.models import Product, Subcategory


class TitleValidator:
    '''Проверка поля title'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        title = value.get('title')

        if len(title) > 300:
            raise ValidationError('Кол-во символов превышает допустимую норму (300 шт.)  !')


class PriceValidator:
    '''Валидатор цены'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        price = value.get('price')

        try:
            int(price)
        except Exception as e:
            raise ValidationError('Неверный формат данных в поле price.')


class SubcategoryValidator:
    '''Валидатор подкатегории'''

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        subcategory = value.get('subcategory')
        result = Subcategory.objects.filter(pk=subcategory)

        if not result:
            raise ValidationError('Подкатегория не найдена!')
