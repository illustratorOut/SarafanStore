from colorama import Fore
from django.core.management import BaseCommand

from store.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category = ['Овощи, фрукты, орехи', 'Хлеб, хлебцы, выпечка', 'Молоко, сыр, яйца, растительные продукты',
                    'Макароны, крупы, мука', 'Вода, соки, напитки', 'Чипсы, снеки, сухофрукты', 'Мясо, птица',
                    'Рыба, морепродукты, икра', 'Колбасы, сосиски, деликатесы', 'Чай, кофе, какао', 'Сладости',
                    'Замороженные продукты', 'Растительные масла, специи, соусы', 'Консервы, соленья, варенье',
                    'Детские товары', 'Канцтовары, книги, творчество', 'Товары для животных', 'Косметика, гигиена',
                    'Бытовая химия, уборка', 'Товары для дома', 'Кухня', 'Выгодные предложения Фикспрайс', ]

        dict_category = {index + 1: {'title': data, 'img': f'category/{index + 1}.png', } for index, data in
                         enumerate(category)}

        for row in dict_category:
            title = dict_category[row]['title']

            if Category.objects.filter(title=title):
                print(f'Категория "{Fore.RED}{title}{Fore.RESET}" уже существует!')
            else:
                product = Category.objects.create(**dict_category[row])
                product.save()
                print(f'Категория {Fore.GREEN}{title}{Fore.RESET} создан!')
