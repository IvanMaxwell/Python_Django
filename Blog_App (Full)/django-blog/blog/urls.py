from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('add/', views.create_post, name='create-post'),
    path('register/', views.register, name='register'),
]
