from datetime import datetime

from django.db import models


# Create your models here.

class profile (models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    description = models.TextField(default='description here')
    location = models.CharField(max_length=1000)
    user_name = models.CharField(max_length=300)

    def __str__(self):
        return self.user_name



