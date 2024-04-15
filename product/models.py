from datetime import datetime
import random
from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_delete
from pathlib import Path


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        db_table = "Category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_category",  kwargs={"category_slug": self.slug})


class NameModel(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        db_table = "Models"
        verbose_name = "Model"
        verbose_name_plural = "Models"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_model", kwargs={"name_model_slug": self.slug})


def _load_to(self, filename):
    ext = filename.split(".")[-1]
    path = datetime.utcnow().strftime("Product/%Y%m%d/")
    f_b_name = hex(random.randint(100000, 999999))
    return f"{path}{f_b_name}.{ext}"


class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name_models = models.ForeignKey(NameModel, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.CharField(max_length=2000)
    price = models.FloatField()
    delivery = models.BooleanField(default=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to=_load_to)

    class Meta:
        db_table = "Product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def get_absolute_url(self):
        return reverse("shop:product_item", args=[self.slug])

    def __str__(self):
        return self.name


def clean_img(img_path: Path):
    try:
        img_path.unlink()
    except OSError:
        ...
    while True:
        img_path = img_path.parent
        try:
            img_path.rmdir()
        except OSError:
            break


@receiver(post_delete, sender=Product)
def del_photo(sender, instance, **kwargs):
    img_path = Path(instance.img.path)
    clean_img(img_path)
