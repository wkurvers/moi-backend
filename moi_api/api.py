from moi_api.models import favorite
from rest_framework import viewsets, permissions
from moi_api.serializer import *
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = favorite.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FavoriteSerializer

