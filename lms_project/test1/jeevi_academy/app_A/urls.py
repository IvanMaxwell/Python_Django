from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),       # 👈 now handles "/"
    path('home/', views.home_view, name='home'),  # 👈 still handles "/home"
]
