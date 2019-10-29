from moi_api.models import user, favorite
from rest_framework import viewsets, permissions
from moi_api.serializer import userSerializer, favoriteSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = userSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = favorite.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = favoriteSerializer
