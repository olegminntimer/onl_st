from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy, reverse

from catalog.models import Product


class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter +=1
        self.object.save()
        return self.object

class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "photo", "category", "price")
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "photo", "category", "price")
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')




def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'home.html')
