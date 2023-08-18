from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
import requests
from .models import User

class KakaoSignInView(View):
    def get(self, request):
        app_key = 'a1a341e711531afc648d821e7e1129f9'
        redirect_uri = 'http://15.164.56.204:8000/users/signin/kakao/callback'
        kakao_auth_api = 'https://kauth.kakao.com/oauth/authorize?response_type=code'

        return redirect (
            f'{kakao_auth_api}&client_id={app_key}&redirect_uri={redirect_uri}'
        )
    

class KakaoSignInCallBackView(View):

    def get(self, request):
        auth_code = request.GET["code"]
        kakao_token_api = 'https://kauth.kakao.com/oauth/token'

        data = {
            'grant_type': 'authorization_code',
            'client_id': 'a1a341e711531afc648d821e7e1129f9',
            'redirect_uri': 'http://localhost:3000/login',
            'code': auth_code
        }

        token_response = requests.post(kakao_token_api, data=data)
        access_token=token_response.json()["access_token"]
        user_info_response = requests.get('https://kapi.kakao.com/v2/user/me', headers={"Authorization": f'Bearer {access_token}'})

        user_info_json = user_info_response.json()
        kakao_name= user_info_json["properties"]["nickname"]
        print(kakao_name)
        # kakao_name= user_info_json["properties"].json()["nickname"]
        kakao_id = user_info_json["id"]

        try:
            # 데이터베이스에서 kakao_id로 사용자 조회
            user = User.objects.get(kakao_id=kakao_id)
        except User.DoesNotExist:
            # 사용자가 없으면 데이터베이스에 등록
            user = User.objects.create(kakao_id=kakao_id,username=kakao_name)
            is_user = False

        # SimpleJWT를 사용하여 JWT 토큰 생성
        access_token = AccessToken.for_user(user)
        refresh_token = RefreshToken.for_user(user)
        
        access_token = str(access_token)
        refresh_token = str(refresh_token)

        response_data = {
            'refresh_token': refresh_token,      # SimpleJWT로 생성된 액세스 토큰
            'access_token' : access_token,
            'is_user' : is_user,
        }

        return JsonResponse(response_data)

def get_user_id(token):
    decoded_token = AccessToken(token)
    user_id = decoded_token.payload.get('user_id')
    return user_id


