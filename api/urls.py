from django.urls import path
from .views import CustomUserApiView, CustomUserDetailApiView


urlpatterns = [
    path('users/', CustomUserApiView.as_view()),
    path('users/<int:pk>/', CustomUserDetailApiView.as_view()),
]