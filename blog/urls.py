from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
]