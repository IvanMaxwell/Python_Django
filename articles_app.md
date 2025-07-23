 # Ariticle app


# Django Articles App Guide — CRUD, Comments & Static CSS 

This guide walks you through building a simple Django app with:

* Create, view, edit, and delete articles
* Add comments to articles
* Use custom HTML templates
* Apply styling via a static CSS file

---

## 1. Project Setup

### Create the project and app

bash

```
django-admin startproject blogproject
cd blogproject
python manage.py startapp articles
```

### Register the app in `blogproject/settings.py`

python

```
INSTALLED_APPS = [
    ...
    'articles',
]
```

---

## 2. Templates Setup

### Folder structure to create

```
articles/
├── templates/
│   └── articles/
│       ├── article_list.html
│       ├── article_detail.html
│       └── article_form.html
```

## Templates files
---

## 1. `article_list.html`

**Path:** `articles/templates/articles/article_list.html`

html

```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>All Articles</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <h1>All Articles</h1>

    <a href="{% url 'article_create' %}">+ New Article</a>

    <ul>
        {% for article in articles %}
            <li>
                <a href="{% url 'article_detail' article.pk %}">{{ article.title }}</a>
                <br>
                <small>Created on {{ article.created_at|date:"d M Y, H:i" }}</small>
            </li>
        {% empty %}
            <li>No articles found.</li>
        {% endfor %}
    </ul>
</body>
</html>
```



---

## 2. `article_detail.html`

**Path:** `articles/templates/articles/article_detail.html`

html

```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ article.title }}</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <h1>{{ article.title }}</h1>

    <p>{{ article.content }}</p>
    <small>Published: {{ article.created_at|date:"d M Y, H:i" }}</small>

    <div>
        <a href="{% url 'article_edit' article.pk %}">Edit</a> |
        <a href="{% url 'article_delete' article.pk %}">Delete</a> |
        <a href="{% url 'article_list' %}">Back to List</a>
    </div>

    <hr>

    <h2>Comments</h2>
    {% for comment in comments %}
        <div>
            <strong>{{ comment.author }}</strong> on {{ comment.created_at|date:"d M Y, H:i" }}<br>
            {{ comment.text }}
        </div>
    {% empty %}
        <p>No comments yet.</p>
    {% endfor %}

    <h3>Add a Comment</h3>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Post Comment</button>
    </form>
</body>
</html>
```

---

## 3. `article_form.html`

**Path:** `articles/templates/articles/article_form.html`

html

```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% if form.instance.pk %}Edit{% else %}New{% endif %} Article</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <h1>{% if form.instance.pk %}Edit{% else %}New{% endif %} Article</h1>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Save</button>
    </form>

    <a href="{% url 'article_list' %}">Back to List</a>
</body>
</html>
```


---

## 3. Models — `articles/models.py`

python

```
# articles/models.py

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)  # Article title
    content = models.TextField()              # Main content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp on creation

    def __str__(self):
        return self.title  # Used in admin panel and shell

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')  # Link to article
    author = models.CharField(max_length=100)  # Name of commenter
    text = models.TextField()                  # Comment body
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author}'

```

---

## 4. Migrations

bash

```
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Forms — `articles/forms.py`

python

```
# articles/forms.py

from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']  # Fields to show in the form

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']

```

---

## 6. Views — `articles/views.py`

python

```
# articles/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm, CommentForm

# List all articles
def article_list(request):
    articles = Article.objects.all().order_by('-created_at')  # Newest first
    return render(request, 'articles/article_list.html', {'articles': articles})

# Show one article + comments
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article  # Link comment to the current article
            comment.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = CommentForm()
    
    return render(request, 'articles/article_detail.html', {
        'article': article,
        'comments': comments,
        'form': form
    })

# Create a new article
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'articles/article_form.html', {'form': form})

# Edit an existing article
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/article_form.html', {'form': form})

# Delete article
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')

```

---

## 7. URLs

### `articles/urls.py`

python

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('article/new/', views.article_create, name='article_create'),
    path('article/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),
]
```

### `blogproject/urls.py`

python

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls')),
]
```

---

## 8. Static Files (CSS)

### Folder structure

```
articles/
├── static/
│   └── css/
│       └── style.css
```

### Example `style.css`

css

```
/* Base styles */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f4f6f8;
    margin: 0;
    padding: 2rem;
    color: #333;
}

/* Headings */
h1, h2, h3 {
    color: #1a1a1a;
}

/* Links */
a {
    color: #2b7cff;
    text-decoration: none;
    font-weight: 500;
}
a:hover {
    text-decoration: underline;
}

/* Article list */
ul {
    list-style: none;
    padding: 0;
}
li {
    margin-bottom: 1rem;
    background-color: #fff;
    padding: 1rem;
    border-radius: 6px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}

/* Buttons */
button, a.button-link {
    background-color: #2b7cff;
    color: #fff;
    padding: 0.6rem 1.2rem;
    border: none;
    border-radius: 4px;
    font-size: 0.9rem;
    cursor: pointer;
    text-decoration: none;
    display: inline-block;
    margin-top: 0.5rem;
}
button:hover, a.button-link:hover {
    background-color: #1a5fce;
}

/* Forms */
form {
    background: #fff;
    padding: 1.5rem;
    border-radius: 6px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    margin-bottom: 2rem;
}
form input, form textarea {
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
}

/* Comments */
.comment {
    background-color: #e9f0ff;
    padding: 0.8rem;
    border-radius: 4px;
    margin-bottom: 1rem;
}
.comment strong {
    display: block;
    margin-bottom: 0.3rem;
}




after adding css the app should look like this ,




<img width="2479" height="1243" alt="image" src="https://github.com/user-attachments/assets/3809c22d-fb65-471e-9c7b-da1c858cd0b8" />


```

---

## 9. settings.py (Static Configuration)

Basic required setting:

python

```
STATIC_URL = '/static/'
```

If you use a global folder like `static/` at the root, then add this:

python

```
import os

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

---

## 10. Run the Server and Test

bash

```
python manage.py runserver
```

Visit in browser:

* [http://127.0.0.1:8000/](http://127.0.0.1:8000/) — Article list
* [http://127.0.0.1:8000/article/new/](http://127.0.0.1:8000/article/new/) — Create article
* [http://127.0.0.1:8000/article/1/](http://127.0.0.1:8000/article/1/) — Article detail with comments

---

## 11. Optional: Admin Panel

### `articles/admin.py`
python
```
from django.contrib import admin
from .models import Article, Comment

admin.site.register(Article)
admin.site.register(Comment)
```

Create admin user:

bash

```
python manage.py createsuperuser
```

Login at:
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## structure of code,


---
