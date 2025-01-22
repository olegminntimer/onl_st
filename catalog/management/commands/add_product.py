from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Добавление продукта в базу данных"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category1, _ = Category.objects.get_or_create(
            name="Овощи",
            description="О́вощи — кулинарный термин, обозначающий съедобную часть (например, плод или клубень) некоторых растений, а также всякую твёрдую растительную пищу, за исключением фруктов, круп и орехов (включение в эту категорию плодовых тел грибов и съедобных водорослей зависит от источника). Кулинарный термин «овощ» может применяться к съедобным плодам, которые с точки зрения ботаники являются ягодами. Овощи являются важной частью рациона человека. Источником овощей в подавляющем большинстве случаев служат овощные культуры, возделываемые сельскохозяйственными предприятиями в промышленных масштабах. Выращиванием овощей занимается овощеводство",
        )

        category2, _ = Category.objects.get_or_create(
            name="Колбасы",
            description="Пищевой продукт; классообразующий тип колбасных изделий, представляющий собой мясной (часто свиной, говяжий или птичий) фарш в продолговатой оболочке. Колбаса может содержать один или несколько видов мяса, например, мясо птиц, различные наполнители, подвергаться температурной обработке (варке, иногда многократной; обжарке; копчению) или ферментации. ",
        )

        products = [
            {
                "name": "Цветная капуста",
                "category": category1,
                "price": "150",
                "created_at": "2025-01-01",
                "updated_at": "2025-01-13",
            },
            {
                "name": "Хрен",
                "category": category1,
                "price": "145",
                "created_at": "2025-01-02",
                "updated_at": "2025-01-10",
            },
            {
                "name": "Репа",
                "category": category1,
                "price": "114",
                "created_at": "2025-01-03",
                "updated_at": "2025-01-14",
            },
            {
                "name": "Чоризо",
                "category": category2,
                "price": "224",
                "created_at": "2025-01-04",
                "updated_at": "2025-01-11",
            },
            {
                "name": "Полукопченая колбаса",
                "category": category2,
                "price": "201",
                "created_at": "2025-01-05",
                "updated_at": "2025-01-12",
            },
            {
                "name": "Салями",
                "category": category2,
                "price": "199",
                "created_at": "2025-01-06",
                "updated_at": "2025-01-13",
            },
        ]

        for product in products:
            product, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Добавление продукта произошло успешно: {product.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Продукт уже добавлен: {product.name}"))
