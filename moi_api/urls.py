from rest_framework import routers
from .api import *
from .views import CreateUserAPIView, CreateUserSearchProfileAPIView
from rest_framework_simplejwt import views as jwt_views
from django.urls import path
urlpatterns = [
	path('storeSearchProfile/', CreateUserSearchProfileAPIView.as_view(), name="storeSearchProfile"),
	path('register/',CreateUserAPIView.as_view(), name="register"),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]