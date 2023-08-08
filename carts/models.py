from django.db import models

from customers.models import Customer
from products.models import Product


#Cart 클래스 : 장바구니 테이블
class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='cart_user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product')
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.user.name} - {self.product.name}"
