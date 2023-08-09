from django.db import models

from sellers.models import Seller


# Category 클래스 : 카테고리 테이블
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Product 클래스 : 상품 테이블
class Product(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    price = models.IntegerField()
    main_image = models.ImageField(blank=True,null=True)
    add_image_1 = models.ImageField(blank=True,null=True)
    add_image_2 = models.ImageField(blank=True,null=True)
    detail = models.TextField()
    uploaded_at = models.DateTimeField()
    sold = models.IntegerField(blank=True, null=True)
    stars = models.IntegerField(blank=True, null=True)
    liked = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='product_seller')

    def __str__(self):
        return self.name

# ProductSize 클래스 : 상품사이즈 테이블
class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    outer_size = models.CharField(max_length=10, blank=True, null=True)
    top_size = models.CharField(max_length=10, blank=True, null=True)
    shoes_size = models.CharField(max_length=10, blank=True, null=True)
    pants_size = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} - Size Info"

# ProductColor 클래스 : 상품색상 테이블
class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name