import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import request
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Category
from catalog.services import get_products_from_cache, get_products_from_category  # , get_products_from_category


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        categories = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['categories'] = categories
        return context

    def get_queryset(self):
        return get_products_from_cache()


class ProductCategoryListView(ListView):
    model = Product

    template_name = "catalog/product_category_list.html"

    def get_context_data(self, **kwargs):
        categories = Category.objects.all()
        context = super().get_context_data(**kwargs)
        context['categories'] = categories
        return context

    def get_queryset(self):
        queryset = get_products_from_category(str(self.kwargs.get("id")))
        return queryset




class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied



class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
