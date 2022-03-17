from django.urls import path
from .views import home, post_detail

urlpatterns = [
    path('', home, name='home'),
    path('post/<str:slug>/', post_detail, name='post-detail')
]