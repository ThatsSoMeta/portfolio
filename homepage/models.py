from django.db import models
from django.utils import timezone

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=25)
    sku = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.product_name
