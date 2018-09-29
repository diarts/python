from django.shortcuts import render, get_object_or_404, get_list_or_404
from . import models


def main_page(request):
    return render(request, 'home_work/index.html', {})


def catalog(request):
    product_list = get_list_or_404(models.Product)
    return render(request, 'home_work/catalog.html', {'product_list': product_list})


def product_description(request, name):
    # name = href.replace('_', ' ')
    product = get_object_or_404(models.Product, name=name)

    return render(request, 'home_work/components/product_description.html', {'product': product})


def contacts(request):
    return render(request, 'home_work/contacts.html', {})
