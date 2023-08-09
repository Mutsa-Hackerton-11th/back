from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from .models import Product
from .serializers import ProductSerializer

"""
API명 : 인기상품목록조회API
설명 : 판매량이 가장 높은 상품 6개를 불러옴
작성자 : 남석현
"""
class PopularProductView(APIView):
    def get(self, request, format=None):
        popular_products = Product.objects.all().order_by('-sold')[:5] #상위 5개 상품
        serializer = ProductSerializer(popular_products, many=True)

        response_data = {
            "check": True,
            "popular_products": []
        }

        for product_data in serializer.data:
            print(product_data)
            popular_product = {
                "product_id": product_data["id"],
                "product_name": product_data["name"]
                # "image": product_data["main_image"]
            }
            response_data["popular_products"].append(popular_product)
        return Response(response_data, status=status.HTTP_200_OK)
        #추후구현 : try-catch로 응답 False일 경우도 구현

