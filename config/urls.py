"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings
from products.views import PopularProductView, NewProductView, CategoryProductsAPIView,\
    SearchProductsAPIView, BrandListAPIView, BrandProductsAPIView, ProductDetailAPIView,\
    ProductOrderAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')), 
    path('sellers/', include('sellers.urls')), 
    path('api/products/best-sellers/',PopularProductView.as_view(),name='popular-products'),
    path('api/products/new-sellers/', NewProductView.as_view(), name='new-products'),
    path('api/products/<str:category>/', CategoryProductsAPIView.as_view(), name='category-products'),
    path('api/products/search/', SearchProductsAPIView.as_view(), name='search-products'),
    path('api/brands/', BrandListAPIView.as_view(), name='brands'),
    path('api/brands/<str:company_name>/', BrandProductsAPIView.as_view(), name='brand-product'),
    path('api/products/detail/<str:pid>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('api/products/order/<str:pid>/', ProductOrderAPIView.as_view(), name='product-orderview'),
]


#이미지 전송관련 url
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
