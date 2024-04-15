from django.http import HttpResponseRedirect
from home.forms import EmailForm
from product.models import Product, Category, NameModel
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from math import ceil
from django.conf import settings


def product(request, category_slug=None, name_model_slug=None):
    category = None
    name_models = None
    categories = Category.objects.all()
    name_model = NameModel.objects.all()
    products = Product.objects.filter(available=True)
    if name_model_slug:
        name_models = get_object_or_404(NameModel, slug=name_model_slug)
        products = products.filter(name_models=name_models)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    form_email = request.session.get("email")
    email = EmailForm(initial=form_email) if form_email is not None else EmailForm()
    cart_product_form = CartAddProductForm()

    return render(request, "product.html", {"email": email,
                                            "category": category,
                                            "categories": categories,
                                            "products": products,
                                            "name_models": name_models,
                                            'name_model': name_model,
                                            'cart_product_form': cart_product_form})


def product_item(request, slug):
    item = get_object_or_404(Product, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    form_email = request.session.get("email")
    email = EmailForm(initial=form_email) if form_email is not None else EmailForm()
    return render(request, "item_product.html", {
        "item": item,
        "email": email,
        'cart_product_form': cart_product_form
    })


