# Generated by Django 4.2.2 on 2025-02-03 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blogs", "0002_article_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите владельца блога",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец блога",
            ),
        ),
    ]
