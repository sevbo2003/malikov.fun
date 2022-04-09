from django.urls import path
from .views import home, post_detail, about_me, notes, like_view, save_view, delete_save_view, by_category, by_tag, saved_posts

urlpatterns = [
    path('', home, name='home'),
    path('post/<str:slug>/', post_detail, name='post-detail'),
    path('about/', about_me, name='about-me'),
    path('notes/', notes, name='notes'),
    path('category/<str:category>/', by_category, name='category'),
    path('tag/<str:tag>/', by_tag, name='tag'),
    path('saved/', saved_posts, name='saved-posts'),

]


urlpatterns += [
    path('like/<int:pk>/', like_view, name='like-post'),
    path('save/<int:pk>/', save_view, name='save-post'),
    path('delete/<int:pk>/', delete_save_view, name='delete-post'),
]