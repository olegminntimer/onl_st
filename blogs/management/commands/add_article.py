from django.core.management.base import BaseCommand
from blogs.models import Article


class Command(BaseCommand):
    help = 'Добавление статьи в базу данных'

    def handle(self, *args, **options):
        Article.objects.all().delete()

        articles = [
            {'title': 'Статья 1', 'content': 'Текст 1 статьи', 'created_at': '2025-01-01', 'is_published': 'True'},
            {'title': 'Статья 2', 'content': 'Текст 2 статьи', 'created_at': '2024-12-15', 'is_published': 'True'},
            {'title': 'Статья 3', 'content': 'Текст 3 статьи', 'created_at': '2024-12-01', 'is_published': 'True'},
            {'title': 'Статья 4', 'content': 'Текст 4 статьи', 'created_at': '2024-10-01', 'is_published': 'True'},
        ]

        for article in articles:
            article, created = Article.objects.get_or_create(**article)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Добавление статьи произошло успешно: {article.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Статья уже добавлена: {article.title}'))
