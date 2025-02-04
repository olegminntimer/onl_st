from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Категория", help_text="Введите название категория")
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание категории",
        help_text="Введите описание категория",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = [
            "name",
        ]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Продукт", help_text="Введите название продукта")
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
    )
    photo = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Фото продукта",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Категория продукта",
        help_text="Введите название категории",
        related_name="products",
    )
    price = models.FloatField(
        blank=True,
        null=True,
        verbose_name="Цена продукта",
        help_text="Введите цену продукта",
    )
    created_at = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Дата создании записи о продукте",
    )
    updated_at = models.DateField(
        auto_now=True,
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Дата внесения последнего изменения",
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Признак публикации",
        help_text="Опубликован ли продукт?",
    )  # признак публикации (булевое поле),
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец продукта",
        help_text="Укажите владельца продукта",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )  # Владелец продукта.

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "category",
            "name",
        ]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]

    def __str__(self):
        return self.name
