from django.urls import path
from . import views

urlpatterns = [
    path('quizzes/', views.quiz_list, name='quiz_list'),
    path('quizzes/add/', views.add_quiz, name='add_quiz'),
]
