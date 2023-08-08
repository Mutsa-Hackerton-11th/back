from django.contrib.auth.models import AbstractUser
from django.db import models
from users.models import User

#Customer 클래스 : 일반회원 테이블
class Customer(User):
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.username