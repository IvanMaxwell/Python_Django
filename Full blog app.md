# Blog_App // needs to change insides


##  Project Summary

* Only one page: `/` – shows blog posts.
* Admin adds posts through Django admin (`/admin/`).
* No user registration or forms.
* Very beginner-friendly structure.

---

##  Project Structure

```
blog_project/
├── blog/
│   ├── templates/
│   │   └── blog/
│   │       └── home.html
│   ├── models.py
│   ├── views.py
│   └── urls.py
|   ├──forms.py
├── blog_project/
│   ├── settings.py
│   └── urls.py
├── db.sqlite3
└── manage.py
```

---

##  Step-by-Step Guide

---

### 1. Create Project & App

bash

```
django-admin startproject blog_project
cd blog_project
python manage.py startapp blog
```

---

### 2. Register App in `settings.py`

**blog\_project/settings.py**

python

```
INSTALLED_APPS = [
    ...
    'blog',
    'django.contrib.auth',
    'django.contrib.messages',
]
```

---

### 3. Configure Templates and Auth Redirects

**In `settings.py`:**

python

```
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

---
### 4. Create BlogPost Model

**blog/models.py**

python

```
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

---

### 5. Migrate Database

bash

```
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Register Model in Admin

**blog/admin.py**

python

```
from django.contrib import admin
from .models import BlogPost

admin.site.register(BlogPost)
```

---

### 7. Create Superuser

bash

```
python manage.py createsuperuser
```

Follow prompts to create an admin account.

---

### ✅ 8. Create Forms

**blog/forms.py**

python

```
from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
```

---
### 9. Create View to Show Posts

**blog/views.py**

python

```
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in new user
            return redirect('blog-home')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})


@login_required

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

```

---

### 10. Create Template


#### 🔹 base.html (optional layout)

html

```
<!DOCTYPE html>
<html>
<head>
    <title>Blog App</title>
</head>
<body>
    {% if user.is_authenticated %}
        <p>Hello, {{ user.username }} | <a href="{% url 'logout' %}">Logout</a></p>
        <a href="{% url 'create_post' %}">Create Post</a>
    {% else %}
        <a href="{% url 'login' %}">Login</a> |
        <a href="{% url 'register' %}">Register</a>
    {% endif %}
    <hr>
    {% block content %}{% endblock %}
</body>
</html>
```

---

#### 🔹 home.html

html

```
{% extends 'blog/base.html' %}

{% block content %}
<h1>Blog Posts</h1>
{% for post in posts %}
    <h2>{{ post.title }}</h2>
    <small>{{ post.created_at }}</small>
    <p>{{ post.content }}</p>
    <hr>
{% empty %}
    <p>No blog posts yet.</p>
{% endfor %}
{% endblock %}
```

---

#### 🔹 register.html

html

```
{% extends 'blog/base.html' %}
{% block content %}
<h2>Register</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Register</button>
</form>
{% endblock %}
```

---

#### 🔹 login.html

html

```
{% extends 'blog/base.html' %}
{% block content %}
<h2>Login</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
{% endblock %}
```

---

#### 🔹 create\_post.html

h

```
{% extends 'blog/base.html' %}
{% block content %}
<h2>Create a New Blog Post</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Post</button>
</form>
{% endblock %}
```

---
---

### 11. Setup URLs

**blog/urls.py**

python

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('add/', views.create_post, name='create-post'),
    path('register/', views.register, name='register'),
]

```

**blog\_project/urls.py**

python

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

---

### 12. Run the Server

bash

```
python manage.py runserver
```


Visit:

* `http://127.0.0.1:8000/` → to view blog posts
* `http://127.0.0.1:8000/admin/` → to log in as admin and add posts

---







