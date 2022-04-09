from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView as logoutview

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # accounts
    path('accounts/', include('allauth.urls')),
    path('account/logout/', logoutview.as_view(), name='logout'),
    # local apps
    path('', include('posts.urls')),
    # api
    path('api/', include('api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
