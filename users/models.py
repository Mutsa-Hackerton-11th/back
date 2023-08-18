from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    kakao_id = models.CharField(max_length=100, blank=True, null=True)
    kakao_token = models.CharField(max_length=200, blank=True, null=True)
    is_user = models.BooleanField(default= False)

    def __str__(self):
        return self.username