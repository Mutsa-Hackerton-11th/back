from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from sellers.models import Seller
from .serializers import ProductSerializer
from sellers.serializers import SellerSerializer

import random

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
            popular_product = {
                "product_id": product_data["id"],
                "product_name": product_data["name"]
                # "image": product_data["main_image"]
            }
            response_data["popular_products"].append(popular_product)
        return Response(response_data, status=status.HTTP_200_OK)
        #추후구현 : try-catch로 응답 False일 경우도 구현

"""
API명 : 신규상품목록조회API
설명 : 가장 최근에 업로드된 가장 높은 상품 6개를 불러옴
작성자 : 남석현
"""
class NewProductView(APIView):
    def get(self, request, format=None):
        new_products = Product.objects.all().order_by('-uploaded_at')[:5] #상위 5개 상품
        serializer = ProductSerializer(new_products, many=True)

        response_data = {
            "check": True,
            "new_products": []
        }

        for product_data in serializer.data:
            new_product = {
                "product_id": product_data["id"],
                "product_name": product_data["name"]
                # "image": product_data["main_image"]
            }
            response_data["new_products"].append(new_product)
        return Response(response_data, status=status.HTTP_200_OK)
        #추후구현 : try-catch로 응답 False일 경우도 구현

"""
API명 : 카테고리별상품목록조회API
설명 : 카테고리별 상품을 조회하는 API
작성자 : 남석현
"""
class CategoryProductsAPIView(APIView):
    def get(self, request, category, format=None):
        products = Product.objects.filter(category__name=category)
        serializer = ProductSerializer(products, many=True)

        response_data = {
            "check": True,
            f"{category}_products": []
        }

        for product in serializer.data:
            seller_id = product['seller']['id']  #외래기 id값 받아오기
            seller = Seller.objects.get(id=seller_id)
            category_product= {
                "product_id": product["id"],
                "name": product["name"],
                # "image": product["main_image"],
                "shop_name": seller.company_name,
                "like_counts": product["liked"]
            }
            response_data[f"{category}_products"].append(category_product)

        return Response(response_data, status=status.HTTP_200_OK)
        # 추후구현 : try-catch로 응답 False일 경우도 구현

"""
API명 : 상품검색API
설명 : 키워드로 상품을 검색하는 API
작성자 : 남석현
"""
class SearchProductsAPIView(APIView):
    def get(self, request, format=None):
        # 데이터 요청
        keyword = request.query_params.get('keyword')
        print("실행")
        print(keyword)

        # 검색어를 포함하는 상품 필터링
        products = Product.objects.filter(name__icontains=keyword)
        serializer = ProductSerializer(products, many=True)

        response_data = {
            "check": True,
            "searched_products": []
        }

        for product in serializer.data:
            seller_id = product['seller']['id']  # 외래기 id값 받아오기
            seller = Seller.objects.get(id=seller_id)
            search_product = {
                "product_id": product["id"],
                "name": product["name"],
                # "image": product["main_image"],
                "shop_name": seller.company_name,
                "like_counts": product["liked"]
            }
            response_data["searched_products"].append(search_product)

        return Response(response_data, status=status.HTTP_200_OK)

"""
API명 : 쇼핑몰목록조회API
설명 : 쇼핑몰 목록을 조회하는 API
작성자 : 남석현
"""
class BrandListAPIView(APIView):
    def get(self, request, format=None):
        brands = Seller.objects.all()
        serializer = SellerSerializer(brands, many=True)

        shuffled_brands = random.sample(serializer.data, len(serializer.data))

        response_data = {
            "check": True,
            "brands": []
        }

        for brannd_data in shuffled_brands:
            brand = {
                "seller_id": brannd_data["id"],
                "company_name": brannd_data["company_name"],
                # "seller_image": brannd_data["main_image"],
                "seller_detail": brannd_data["company_info"]
            }
            response_data["brands"].append(brand)
        return Response(response_data, status=status.HTTP_200_OK)
        #추후구현 : try-catch로 응답 False일 경우도 구현

"""
API명 : 쇼핑몰별상품목록조회API
설명 : 쇼핑몰별 상품을 조회하는 API
작성자 : 남석현
"""
class BrandProductsAPIView(APIView):
    def get(self, request, company_name, format=None):
        brand = Seller.objects.get(company_name=company_name)
        products = Product.objects.filter(seller=brand)
        serializer = ProductSerializer(products, many=True)

        response_data = {
            "check": True,
            "brand_products": []
        }

        for product in serializer.data:
            brand_product= {
                "product_id": product["id"],
                "name": product["name"],
                # "image": product["main_image"],
                "shop_name": brand.company_name,
                "like_counts": product["liked"]
            }
            response_data["brand_products"].append(brand_product)

        return Response(response_data, status=status.HTTP_200_OK)
        # 추후구현 : try-catch로 응답 False일 경우도 구현