from django.db import models

from customers.models import Customer
from products.models import Product


class Liked(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='liked_user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='liked_product')

    def __str__(self):
        return f"{self.user} - {self.product}"
