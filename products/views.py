from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductSize, ProductColor
from sellers.models import Seller
from .serializers import ProductSerializer, CategorySerializer
from sellers.serializers import SellerSerializer

import random
import datetime

"""
API명 : 인기상품목록조회API
설명 : 판매량이 가장 높은 상품 6개를 불러옴
작성자 : 남석현
"""
class PopularProductView(APIView):
    def get(self, request, format=None):
        popular_products = Product.objects.all().order_by('-sold')
        serializer = ProductSerializer(popular_products, many=True)

        response_data = {
            "check": True,
            "popular_products": []
        }

        for product_data in serializer.data:
            popular_product = {
                "product_id": product_data["id"],
                "product_name": product_data["name"],
                "images": [product_data["main_image"],product_data["add_image_1"]],
                "product_price" : product_data["price"],
                "like_counts": product_data["liked"],
                "category": product_data["category"]["name"]
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
        new_products = Product.objects.all().order_by('-uploaded_at')
        serializer = ProductSerializer(new_products, many=True)

        response_data = {
            "check": True,
            "new_products": []
        }

        for product_data in serializer.data:
            new_product = {
                "product_id": product_data["id"],
                "product_name": product_data["name"],
                "images": [product_data["main_image"],product_data["add_image_1"]],
                "product_price": product_data["price"],
                "like_counts": product_data["liked"],
                "category": product_data["category"]["name"],
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
            "products": []
        }

        for product in serializer.data:
            seller_id = product['seller']['id']  #외래기 id값 받아오기
            seller = Seller.objects.get(id=seller_id)
            category_product= {
                "product_id": product["id"],
                "name": product["name"],
                "product_price": product["price"],
                "image": product["main_image"],
                "shop_name": seller.company_name,
                "like_counts": product["liked"],
                "category": product["category"]["name"],
                "keyword": product["simple_info"]

            }
            response_data["products"].append(category_product)
            # hot, new 추가
            if product["sold"] > 100:
                category_product["hot"] = True
            if (datetime.datetime.now().day - datetime.datetime.strptime(product["uploaded_at"], '%Y-%m-%dT%H:%M:%S%z').day) < 7:
                category_product["new"] = True

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
                "image": product["main_image"],
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
                "seller_image": brannd_data["company_image"],
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
            "products": [],
            "categorys": set()
        }

        for product in serializer.data:
            brand_product= {
                "product_id": product["id"],
                "name": product["name"],
                "product_price": product["price"],
                "image": product["main_image"],
                "shop_name": brand.company_name,
                "like_counts": product["liked"],
                "category": product["category"]["name"],
                "keyword": product["simple_info"]

            }
            response_data["products"].append(brand_product)
            response_data["categorys"].add(product["category"]["name"])
            if product["sold"] > 100:
                brand_product["hot"] = True
            if (datetime.datetime.now().day - datetime.datetime.strptime(product["uploaded_at"], '%Y-%m-%dT%H:%M:%S%z').day) < 7:
                brand_product["new"] = True

        return Response(response_data, status=status.HTTP_200_OK)
        # 추후구현 : try-catch로 응답 False일 경우도 구현

"""
API명 : 상품상세내용조회API
설명 : 상품의 상세내용을 조회하는 API
작성자 : 남석현
"""
class ProductDetailAPIView(APIView):
    def get(self, request, pid):
        try:
            product = Product.objects.get(id=pid)
            category = product.category.name
            sizes = ProductSize.objects.filter(product=product)
            colors = ProductColor.objects.filter(product=product)
            serializer = ProductSerializer(product)
        except Product.DoesNotExist:
            return Response({"check": False, "message": "Product not found"}, status=404)

        size_field = ["아우터_size", "상의_size", "신발_size", "하의_size"]
        category_size_field = f'{category}_size'

        if category_size_field in size_field:
            response_data = {
                "check": True,
                "product_id": product.id,
                "product_name": product.name,
                "images": [serializer.data["main_image"],serializer.data["add_image_1"],serializer.data["add_image_2"],serializer.data["add_image_3"]],
                "shop_name": product.seller.company_name,
                "price": product.price,
                "rating": product.stars,
                "category": category,
                "size": [getattr(size, category_size_field) for size in sizes],
                "color": [color.name for color in colors],
                "keyword": product.simple_info,
                "details": [product.detail_1,product.detail_2],
                "like_counts": product.liked,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            response_data = {
                "check": True,
                "product_id": product.id,
                "product_name": product.name,
                "images": [serializer.data["main_image"],serializer.data["add_image_1"],serializer.data["add_image_2"],serializer.data["add_image_3"]],
                "shop_name": product.seller.company_name,
                "price": product.price,
                "rating": product.stars,
                "category": category,
                "color": [color.name for color in colors],
                "details": [product.detail_1,product.detail_2],
                "like_counts": product.liked,
            }
            return Response(response_data, status=status.HTTP_200_OK)

"""
API명 : 상품주문화면API
설명 : 상품의 주문화면에 들어갈 내용을 조회하는 API
작성자 : 남석현
"""
class ProductOrderAPIView(APIView):
    def get(self, request, pid, format=None):
        try:
            product = Product.objects.get(id=pid)
        except Product.DoesNotExist:
            return Response({"check": False, "message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product)

        response_data = {
            "check": True,
            "product_id": serializer.data["id"],
            "product_name": serializer.data["name"],
            "image": serializer.data["main_image"],
            "price": serializer.data["price"]
        }

        return Response(response_data, status=status.HTTP_200_OK)