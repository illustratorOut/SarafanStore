# Generated by Django 5.0.6 on 2024-06-21 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_subcategory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=10, verbose_name='Цена'),
        ),
    ]
