# gallery/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('register-artist/', views.register_artist, name='register_artist'),  # Registration URL
    path('artists/', views.artist_list, name='artist_list'),
    path('artworks/', views.artwork_list, name='artwork_list'),
    path('exhibitions/', views.exhibition_list, name='exhibition_list'),
]