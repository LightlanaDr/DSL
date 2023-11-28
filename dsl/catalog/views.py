from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.views import View
from .models import Product, Category, ImagesProducts
from django.contrib.auth.hashers import check_password
from cart.forms import CartAddProductForm


def category_products(request):
    """ Представление для списка категорий и продуктов"""
    # category_slug = None
    status = 'Опубликовано'
    categories = Category.objects.filter(status=status).all()
    category = None
    products = Product.objects.all()
    form = CartAddProductForm()
    return render(request, 'catalog/product_detail2.html', {'category': category, 'categories': categories,
                                                            'products': products,
                                                            "form": form})


def cat_slug_products(request, category_slug=None):
    """ Представление для списка категорий и продуктов по категориям"""
    status = 'Опубликовано'
    categories = Category.objects.filter(status=status).all()
    category = None
    products = None
    form = CartAddProductForm()
    if category_slug:
        category = Category.objects.get(id=category_slug)
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    return render(request, 'catalog/product_detail2.html', {'category': category, 'categories': categories,
                                                            'products': products,
                                                            "form": form})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    form = CartAddProductForm()
    return render(request, 'catalog/test.html', {"product": product,
                                                 "form": form})


def get_slug_product(request, product_id=None):
    """ Представление для вывода продукта на отдельной странице"""
    product = None
    images = None
    form = CartAddProductForm()
    if product_id:
        product = Product.objects.get(id=product_id)
        images = ImagesProducts.objects.filter(product=product)
    # else:
    #     products = Product.objects.all()
    return render(request, 'catalog/product_id.html', {'images': images, 'product': product,
                                                       "form": form})


# def get_slug_product(request, product_slug=None):
#     """ Представление для вывода продукта на отдельной странице"""
#     product = None
#     images = None
#     form = CartAddProductForm()
#
#     if product_slug:
#         product = Product.objects.get(id=product_slug)
#         images = ImagesProducts.objects.filter(product=product)
#         image1 = images[0]
#         image2 = images[1]
#         image3 = images[2]
#         # else:
#         #     products = Product.objects.all()
#         return render(request, 'catalog/product_id2.html', {'images': images, 'product': product,
#                                                             "form": form, 'image1': image1, 'image2': image2,
#                                                             'image3': image3, })
