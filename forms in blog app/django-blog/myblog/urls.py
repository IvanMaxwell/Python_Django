"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from blog.views import home, post_create, post_edit, post_delete

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', home, name='home'),  # Home page
    path('post/new/', post_create, name='post_create'),  # Create
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),  # Edit
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),  # Delete
]


