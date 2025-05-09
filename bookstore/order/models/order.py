from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    product = models.ManyToManyField(Product, blank=False)

    def __str__(self):
        return f"Order {self.id}"