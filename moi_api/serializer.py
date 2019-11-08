from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import favorite  # import model
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

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

class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'})

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')
        write_only_fields = ('password')
        read_only_fields = ('is_staff', 'is_superuser', 'is_active',)

    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user