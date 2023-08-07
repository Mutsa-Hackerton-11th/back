from django.db import models


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
    main_image = models.ImageField()
    add_image_1 = models.ImageField()
    add_image_2 = models.ImageField()
    detail = models.TextField()
    uploaded_at = models.DateTimeField()
    sold = models.IntegerField()
    stars = models.IntegerField()
    liked = models.DecimalField(max_digits=2,decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #기업회원 외래키 추가

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