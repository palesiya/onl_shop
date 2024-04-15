from django.contrib import admin
from product.models import Category, NameModel, Product


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(NameModel)
class NameModel(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "img", "available", "created", "updated"]
    list_filter = ["available", "created", "updated"]
    list_editable = ["price", "available"]
    prepopulated_fields = {"slug": ("name",)}

