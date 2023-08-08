from django.contrib.auth.models import AbstractUser
from django.db import models
from users.models import User


# Seller 클래스 : 기업회원 테이블
class Seller(User):
    company_name = models.CharField(max_length=100)
    company_level = models.IntegerField(default=1)  # 디폴트 1
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    certificate = models.ImageField(null=True)  # 업로드 위치 추가
    copy_bankbook = models.ImageField(null=True)  # 업로드 위치 추가
    company_url = models.URLField(null=True)
    is_approved = models.BooleanField(default=False)
    company_image = models.ImageField(null=True)  # 업로드 위치 추가
    company_info = models.TextField(null=True)

    def __str__(self):
        return self.username
