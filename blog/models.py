from django.db import models


class Article(models.Model):

    title = models.CharField(
        max_length=150,
        verbose_name="Название статья",
        help_text="Введите название статьи"
    ) # заголовок,
    content = models.TextField(
        blank=True,
        null=True,
        verbose_name="Содержимое статьи",
        help_text="Что-нибудь напишите"
    ) # содержимое,
    preview = models.ImageField(
        upload_to="blog/preview",
        blank=True,
        null=True,
        verbose_name="Превью статьи",
        help_text="Загрузите изображение для превью статьи",
    ) # превью (изображение),
    created_at = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Дата создании статьи"
    ) # дата создания,
    is_published = models.BooleanField(default=False) # признак публикации (булевое поле),
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0
    ) # количество просмотров.
