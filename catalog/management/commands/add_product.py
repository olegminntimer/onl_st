from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Добавление продукта в базу данных'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Колбасы', description='Колбасы варёные, полукопчёные')

        products = [
            {'name': 'Докторская', 'category': category, 'price': '150', 'created_at': '2025-01-01', 'updated_at': '2025-01-13'},
            {'name': 'Молочная', 'category': category, 'price': '145', 'created_at': '2025-01-02', 'updated_at': '2025-01-10'},
            {'name': 'Южная', 'category': category, 'price': '114', 'created_at': '2025-01-03', 'updated_at': '2025-01-14'},
        ]

        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Добавление продукта произошло успешно: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт уже добавлен: {product.name}'))
