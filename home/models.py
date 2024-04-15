from django.db import models


class Email(models.Model):
    email = models.EmailField(verbose_name="Email")

    class Meta:
        db_table = "email"
