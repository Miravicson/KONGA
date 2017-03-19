from django.db import models


# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    user_name = models.CharField(max_length=300)
    email = models.EmailField(default='Enter your email')
    password = models.CharField(max_length=100, default='Enter password')
    phone_number = models.CharField( max_length=14, default='Enter your phone number')
    location = models.CharField(max_length=1000)

    def __str__(self):
        return self.user_name
