from django.db import models

from users.models import User


class Article(models.Model):

    title = models.CharField(
        max_length=150, verbose_name="Название", help_text="Введите название статьи"
    )  # заголовок,
    content = models.TextField(
        blank=True,
        null=True,
        verbose_name="Текст",
        help_text="Это произведение будет лучшим!",
    )  # содержимое,
    preview = models.ImageField(
        upload_to="article/preview",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите изображение",
    )  # превью (изображение),
    created_at = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name="Дата",
        help_text="Введите дату написания статьи",
    )  # дата создания,
    is_published = models.BooleanField(
        default=True,
        verbose_name="Публикация",
        help_text="Опубликована ли статья?",
    )  # признак публикации (булевое поле),
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )  # количество просмотров.
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец блога",
        help_text="Укажите владельца блога",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )  # Владелец блога.

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title
