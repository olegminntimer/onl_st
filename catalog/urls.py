from django.urls import path
from django.conf.urls.static import static
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, contact
from django.conf import settings

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('contact/', contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)