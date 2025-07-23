# Basic_blog_app

* A beginner-friendly Django blog app with a single home page.
* All blog posts are displayed on the homepage using a simple template.
* No forms or user input — content is added only by the admin.
* Admin adds posts through the Django admin panel.
* Uses a basic model with title, content, and timestamp.
* Great for learning Django models, views, templates, and admin integration.


---

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
├── blog_project/
│   ├── settings.py
│   └── urls.py
├── db.sqlite3
└── manage.py
```

---

## 🛠 Step-by-Step Guide

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
]
```

---

### 3. Create BlogPost Model

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

### 4. Migrate Database

bash

```
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Register Model in Admin

**blog/admin.py**

python

```
from django.contrib import admin
from .models import BlogPost

admin.site.register(BlogPost)
```

---

### 6. Create Superuser

bash

```
python manage.py createsuperuser
```

Follow prompts to create an admin account.

---

### 7. Create View to Show Posts

**blog/views.py**

python

```

from django.shortcuts import render
from .models import BlogPost

def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})
```

---

### 8. Create Template

**blog/templates/blog/home.html**

html

```
<!DOCTYPE html>
<html>
<head>
    <title>Simple Blog</title>
</head>
<body>
    <h1>Welcome to the Blog</h1>
    <hr>
    {% for post in posts %}
        <h2>{{ post.title }}</h2>
        <small>{{ post.created_at }}</small>
        <p>{{ post.content }}</p>
        <hr>
    {% empty %}
        <p>No blog posts yet.</p>
    {% endfor %}
</body>
</html>
```

---

### 9. Setup URLs

**blog/urls.py**

python

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
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

### 10. Run the Server

bash

```
python manage.py runserver
```

Visit:

* `http://127.0.0.1:8000/` → to view blog posts
* `http://127.0.0.1:8000/admin/` → to log in as admin and add posts

---

