from rest_framework import serializers
from .models import Category, Product, ProductSize, ProductColor
from sellers.serializers import SellerSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = '__all__'

class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    seller = SellerSerializer()
    sizes = ProductSizeSerializer(many=True)
    colors = ProductColorSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'