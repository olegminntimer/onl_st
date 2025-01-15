from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, contact, ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    # path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('contact/', contact, name='contact'),
]