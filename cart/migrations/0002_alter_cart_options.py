# Generated by Django 5.0.6 on 2024-06-25 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ('release_date',), 'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
    ]
