from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

from store.services import unique_slugify
from users.models import User

NULLABLE = {
    'blank': True,
    'null': True
}


class Category(models.Model):
    '''Модель Категории'''
    title = models.CharField(max_length=300, verbose_name='Название')
    slug = models.CharField(verbose_name='Альт.название', max_length=255, blank=True, unique=True)
    img = models.ImageField(upload_to='category', verbose_name='Изображение', **NULLABLE)

    release_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор продукта', **NULLABLE)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'{self.__class__.__name__}({self.title})'

    def save(self, *args, **kwargs):
        """Сохранение полей модели при их отсутствии заполнения"""
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        # ordering = ('title',)


class Subcategory(models.Model):
    '''Модель Подкатегории'''
    title = models.CharField(max_length=300, verbose_name='Название')
    slug = models.CharField(verbose_name='Альт.название', max_length=255, blank=True, unique=True)
    img = models.ImageField(upload_to='subcategory', verbose_name='Изображение', **NULLABLE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    release_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор продукта', **NULLABLE)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'{self.__class__.__name__}({self.title})'

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        # ordering = ('title',)


class Product(models.Model):
    '''Модель продукта'''
    title = models.CharField(max_length=300, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    slug = models.CharField(verbose_name='Альт.название', max_length=255, blank=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=3, verbose_name='Цена')
    img = models.ImageField(upload_to='product', verbose_name='Изображение', **NULLABLE)

    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория')

    release_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор продукта', **NULLABLE)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'{self.__class__.__name__}({self.title})'

    def save(self, *args, **kwargs):
        """
        Сохранение полей модели при их отсутствии заполнения
        """
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('title',)
