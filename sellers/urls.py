from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SellerSignUpView.as_view(), name='seller-signup'),
]
