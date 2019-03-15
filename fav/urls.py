from django.urls import path, include
from . import views



urlpatterns = [
    path('about/', views.about, name='about'),
    path('fav/', views.fav, name='fav'),
    ]
