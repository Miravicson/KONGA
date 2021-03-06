from rest_framework import serializers
from .models import Orders, User, Profile

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class OrderSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'