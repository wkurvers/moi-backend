from rest_framework import routers
from .api import *
from .views import *
router = routers.DefaultRouter()
router.register('api/user', UserViewSet, basename='user')
router.register('api/favorite', FavoriteViewSet, basename='favorite')
urlpatterns = router.urls