# ArtGalleryManagement/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', include('gallery.urls')),  # Include your gallery app URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Custom login URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Custom logout URL
]