from rest_framework import serializers
from .models import user,favorite  # import model


# Create a class
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

class favoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = favorite
        fields = '__all__'