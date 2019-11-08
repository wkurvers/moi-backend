from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import favorite  # import model
from django.contrib.auth.models import User

# Create a class
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email','created_at')

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = favorite
        fields = '__all__'

class MessageSerializer(serializers.Serializer):
    message = serializers.CharField()