from rest_framework import serializers
from .models import Cart
from customers.serializers import CustomerSerializer
from products.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    user = CustomerSerializer()
    product = ProductSerializer()

    class Meta:
        model = Cart
        fields = '__all__'