from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('post',views.post_message,name='post_message'),


]


