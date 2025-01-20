from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Категория", help_text="Введите название категория"
    )
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
    name = models.CharField(
        max_length=150, verbose_name="Продукт", help_text="Введите название продукта"
    )
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

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "category",
            "name",
        ]

    def __str__(self):
        return self.name
