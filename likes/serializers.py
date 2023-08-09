from rest_framework import serializers
from .models import Liked
from customers.serializers import CustomerSerializer
from products.serializers import ProductSerializer

class LikedSerializer(serializers.ModelSerializer):
    user = CustomerSerializer()
    product = ProductSerializer()

    class Meta:
        model = Liked
        fields = '__all__'