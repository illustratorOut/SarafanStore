from django.conf import settings
from django.db import models
from django.utils import timezone
from product.models import Product
from users.models import User

NULLABLE = {
    'blank': True,
    'null': True
}


class Cart(models.Model):
    '''Модель Корзины'''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class CartProduct(models.Model):
    '''Модель Продукты корзины'''
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина-Продукт', **NULLABLE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    release_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    def __str__(self):
        return str(self.product)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.quantity})'

    class Meta:
        verbose_name = "Продукты корзины"
        verbose_name_plural = "Продукты корзины"
        ordering = ('release_date',)
