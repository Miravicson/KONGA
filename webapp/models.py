from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    user_name = models.CharField(max_length=300)
    email = models.EmailField(default='Enter your email')
    password = models.CharField(max_length=100, default='Enter password')
    phone_number = models.CharField(max_length=14, default='Enter your phone number')
    location = models.CharField(max_length=1000)

    def __str__(self):
        return self.user_name


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    proxy_first_name = models.CharField(max_length=300, default='pfn')
    proxy_last_name = models.CharField(max_length=300, default='pln')
    proxy_phone_number = models.CharField(max_length=14, default='Enter the your proxy user phone number')
    is_registered_to_kongapay = models.BooleanField(default=False)
