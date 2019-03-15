from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('fav/', include('fav.urls')),
]