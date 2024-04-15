from django.db import models


class Review(models.Model):
    name = models.CharField(max_length=30, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    product_name = models.TextField(max_length=30, verbose_name="product name")
    review = models.TextField(max_length=300, verbose_name="Message text")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "review"
        verbose_name = "review"
        verbose_name_plural = "reviews"
