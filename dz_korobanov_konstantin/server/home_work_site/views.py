from django.shortcuts import render
from . import products


def main_page(request):
    return render(request, 'home_work/index.html', {})


def catalog(request):
    return render(request, 'home_work/catalog.html', {})


def product_description(request):
    product = str(request)[20:-3]
    return render(request, 'home_work/components/product_description.html', {'product': products.products_dict[product]})


def contacts(request):
    return render(request, 'home_work/contacts.html', {})
