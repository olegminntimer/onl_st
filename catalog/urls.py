from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, contact, product_list, product_detail

app_name = 'catalog'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    # path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('contact/', contact, name='contact'),
]