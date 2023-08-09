from django.contrib import admin
from .models import Category, Product, ProductSize, ProductColor

# Category 모델 등록
admin.site.register(Category)

# ProductSize 모델 등록
class ProductSizeInline(admin.TabularInline):
    model = ProductSize

# ProductColor 모델 등록
class ProductColorInline(admin.TabularInline):
    model = ProductColor

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductSizeInline,
        ProductColorInline,
    ]