from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from rest_framework.response import Response
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
        auth_code = request.GET.get('code')
        kakao_token_api = 'https://kauth.kakao.com/oauth/token'
        data = {
            'grant_type' : 'authorization_code',
            'client_id' : 'a1a341e711531afc648d821e7e1129f9',
            'redirection_uri' : 'http://15.164.56.204:8000/users/signin/kakao/callback/',
            'code' : auth_code,
        }

        token_response = requests.post(kakao_token_api, data = data)

        access_token = token_response.json().get('access_token')

        user_info_response = requests.get('https://kapi.kakao.com/v2/user/me', headers={"Authorization": f'Bearer {access_token}'})

        user_info_json = user_info_response.json()
        kakao_id = user_info_json.get('id')

        # 데이터베이스에서 kakao_id 사용자를 확인합니다.
        try:
            user = User.objects.get(kakao_id=kakao_id)
        except User.DoesNotExist:
            # 사용자 정보가 없다면 회원가입 페이지로  리다이렉트되며, 끝 지점에 kakao_id를 쿼리 매개 변수로 첨부합니다.
            return Response({"kakao_id": kakao_id})

        # 사용자 정보가 있다면 JsonResponse를 사용하여 kakao_id를 프론트엔드로 보내줍니다.
        return JsonResponse({"kakao_id": kakao_id})