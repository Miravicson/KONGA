from django.contrib import admin
from .models import Profile

# Register your models here.
# class Profile(admin.ModelAdmin):
#     class Meta:
#         model = Profile

admin.site.register(Profile)

