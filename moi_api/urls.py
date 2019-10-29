from rest_framework import routers
from .api import UserViewSet, FavoriteViewSet

router = routers.DefaultRouter()
router.register('api/user', UserViewSet, 'user')
router.register('api/favorite', FavoriteViewSet, 'favorite')

urlpatterns = router.urls
