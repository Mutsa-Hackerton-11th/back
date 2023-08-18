from django.urls import path
from . import views
from .views import KakaoSignInView, KakaoSignInCallBackView

urlpatterns = [
    path('signin/kakao/', KakaoSignInView.as_view(), name='kakao-signin'),
    path('signin/kakao/callback', KakaoSignInCallBackView.as_view(), name='kakao-callback'),
]
