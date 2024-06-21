from django.db import models
from django.utils import timezone

from product.models import Product
from users.models import User


class Cart(models.Model):
    '''Модель Корзины'''
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кол-во')
    release_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    def __str__(self):
        return self.product

    def __repr__(self):
        return f'{self.__class__.__name__}({self.product})'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
