from django.db import models
from django.utils import timezone

from users.models import User

NULLABLE = {
    'blank': True,
    'null': True
}


class Product(models.Model):
    '''Модель продукта'''
    title = models.CharField(max_length=300, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    slug = models.CharField(max_length=300, verbose_name='Имя')
    price = models.PositiveIntegerField(default=3, verbose_name='Цена')
    photo = models.ImageField(upload_to='users', verbose_name='Фото', **NULLABLE)

    release_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор продукта', **NULLABLE)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'{self.__class__.__name__}({self.title})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('title',)
