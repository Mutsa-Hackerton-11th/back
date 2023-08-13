from django.shortcuts import redirect, render
from django.views import View
from .models import Seller
from .serializers import SellerSerializer

class SellerSignUpView(View):
    def post(self, request):
        sName = request.POST.get('sName')
        sPost = request.POST.get('sPost')
        sAddress = request.POST.get('sAddress')
        sPhone = request.POST.get('sPhone')
        sEmail = request.POST.get('sEmail')

        try:
            seller = Seller.objects.get(username=sEmail)
            # 이미 등록된 기업 회원이면 로그인 화면으로 이동하도록 설정
            return redirect('users:login')
        except Seller.DoesNotExist:
            seller_data = {
                'username': sEmail,
                'password': '',  # 비밀번호는 나중에 설정하거나 사용자가 설정할 수 있도록
                'company_name': sName,
                'postal_code': sPost,
                'address': sAddress,
                'phone_number': sPhone,
                'email': sEmail,
            }

            serializer = SellerSerializer(data=seller_data)
            if serializer.is_valid():
                serializer.save()
                # 회원가입 성공 시 로그인 화면으로 이동하도록 설정
                return redirect('users:login')
            else:
                # 유효성 검사에 실패한 경우 다시 회원가입 화면을 띄워줍니다.
                return render(request, 'sellers/seller_signup.html', {'errors': serializer.errors})
