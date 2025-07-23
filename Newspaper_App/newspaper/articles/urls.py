from django.urls import path

from accounts import views
from .views import Articleslistview,Articlesdetailview,AritcleEditView,AritcleDeleteView,ArticleCreateView

urlpatterns=[
    path('articles/',Articleslistview.as_view(),name='articles'),
    path('article/<int:pk>/',Articlesdetailview.as_view(),name='article_detail'),
    path('article/edit/<int:pk>',AritcleEditView.as_view(),name='article_edit'),
    path('article/<int:pk>/delete/', AritcleDeleteView.as_view(), name='article_delete'),
    path('articles/create/', ArticleCreateView.as_view(), name='article_create')


]