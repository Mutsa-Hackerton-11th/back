from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
import requests

class KakaoSignInView(View):
    def get(self, request):
        app_key = 'a1a341e711531afc648d821e7e1129f9'
        redirect_uri = 'http://localhost:8000/users/signin/kakao/callback'
        kakao_auth_api = 'https://kauth.kakao.com/oauth/authorize?response_type=code'

        return redirect (
            f'{kakao_auth_api}&client_id={app_key}&redirect_uri={redirect_uri}'
        )

class KakaoSignInCallBackView(View):
    def get(self, request):
        auth_code = request.GET.get('code')
        kakao_token_api = 'https://kauth.kakao.com/oauth/token'
        data = {
            'grant_type' : 'authorization_code',
            'client_id' : 'a1a341e711531afc648d821e7e1129f9',
            'redirection_uri' : 'http://localhost:8000/users/signin/kakao/callback',
            'code' : auth_code,
        }

        token_response = requests.post(kakao_token_api, data = data)

        access_token = token_response.json().get('access_token')

        user_info_response = requests.get('https://kapi.kakao.com/v2/user/me', headers={"Authorization": f'Bearer ${access_token}'})

        return JsonResponse(token_response.json())