from django.contrib import admin

from blogs.models import Article


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
        "created_at",
        "is_published",
        "views_counter",
    )
    search_fields = ("title",)
