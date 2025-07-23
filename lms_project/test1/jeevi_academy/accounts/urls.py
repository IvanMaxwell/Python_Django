from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/teacher/', views.teacher_signup, name='teacher_signup'),
    path('signup/student/', views.student_signup, name='student_signup'),

]
