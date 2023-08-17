from django.urls import path
from . import views
from users.views import KakaoSignInView, KakaoSignInCallBackView
from .views import  SellerSignUpAPIView

urlpatterns = [
    path('signin/kakao/', KakaoSignInView.as_view(), name='kakao-signin'),
    path('signin/kakao/callback/', KakaoSignInCallBackView.as_view(), name='kakao-callback'),
    path('signup/', SellerSignUpAPIView.as_view(), name='seller-signup'),
]
