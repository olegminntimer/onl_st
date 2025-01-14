from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Product


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_detail.html', context)


def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'home.html')
