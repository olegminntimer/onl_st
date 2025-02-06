from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


@staticmethod
def get_products_from_cache():
    """Получает данные по продукту из кэша. Если кэш пустой, то получает данные из базы данных"""
    if CACHE_ENABLED:
        key = "product_list"
        products = cache.get(key)
        if products is None:
            products = Product.objects.all()
            cache.set(key, products)
        return products
    return Product.objects.all()


@staticmethod
def get_products_from_category(category):
    products = Product.objects.filter(category=category)
    return products
