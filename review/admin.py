from django.contrib import admin
from review.models import Review


@admin.register(Review)
class NameModel(admin.ModelAdmin):
    list_display = ["name", "review", "created", "product_name"]

