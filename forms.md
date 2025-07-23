Forms in django


To learn forms in django we will be adding customize add page in blog app for users adds **Create, Edit, and Delete** functionality to your existing Django Blog app using Django forms and custom HTML templates, with inline CSS and code comments for clarity.

---

# Django Blog App – Add Create, Edit, Delete (with Forms)

This guide continues from your existing read-only blog. We will:

* Add views for creating, editing, and deleting posts
* Create custom HTML templates for each
* Use Django’s `ModelForm` to handle forms
* Templates use inline CSS
* URLs named for easy access: `post_create`, `post_edit`, `post_delete`
`

---

## 1. Create a Django Form

In `blog/forms.py` (create the file if it doesn't exist):

```python
from django import forms  # Django's forms module
from .models import BlogPost  # Import the BlogPost model

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost  # Link form to BlogPost model
        fields = ['title', 'content']  # Include these fields in the form
```

---

## 2. Update Views for CRUD

In `blog/views.py`, import necessary tools:

```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm
```

### View to create a new post

```python
def post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)  # Bind data to form
        if form.is_valid():
            form.save()  # Save post to DB
            return redirect('home')  # Redirect to homepage
    else:
        form = BlogPostForm()  # Show empty form
    return render(request, 'post_form.html', {'form': form, 'action': 'Create'})
```

### View to edit an existing post

```python
def post_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)  # Get post or 404
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)  # Bind data to existing instance
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'post_form.html', {'form': form, 'action': 'Edit'})
```

### View to delete a post

```python
def post_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()  # Delete post
        return redirect('home')
    return render(request, 'post_confirm_delete.html', {'post': post})
```

---

## 3. Update `urls.py`

In `myblog/urls.py`:

```python
from django.contrib import admin
from django.urls import path
from blog.views import home, post_create, post_edit, post_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Home page
    path('post/new/', post_create, name='post_create'),  # Create
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),  # Edit
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),  # Delete
]
```

---

## 4. Update Templates

### `templates/home.html`

Update your homepage template to include **edit/delete links** and a **create button**.

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Blog</title>
    <style>
        body { font-family: sans-serif; background: #f4f4f4; margin: 0; padding: 0; }
        .container { max-width: 800px; margin: 40px auto; background: #fff; padding: 30px; border-radius: 8px; }
        h1 { text-align: center; }
        a.button { background: #28a745; color: white; padding: 8px 12px; text-decoration: none; border-radius: 4px; }
        a.button:hover { background: #218838; }
        .post-actions { margin-top: 5px; }
        .post-actions a { margin-right: 10px; color: #007bff; }
        .post-actions a:hover { text-decoration: underline; }
    </style>
</head>
<body>
<div class="container">
    <h1>All Blog Posts</h1>
    <a href="{% url 'post_create' %}" class="button">Create New Post</a>
    <ul>
        {% for post in posts %}
            <li>
                <strong>{{ post.title }}</strong><br>
                {{ post.content }}
                <div class="post-actions">
                    <a href="{% url 'post_edit' post.pk %}">Edit</a>
                    <a href="{% url 'post_delete' post.pk %}">Delete</a>
                </div>
            </li>
        {% empty %}
            <li>No posts available.</li>
        {% endfor %}
    </ul>
</div>
</body>
</html>
```


![image](https://github.com/user-attachments/assets/ad7250a1-58a2-445f-b350-7bb6eba5efc2)



---

### `templates/post_form.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ action }} Post</title>
    <style>
        body { font-family: sans-serif; background: #f5f5f5; }
        .container { max-width: 600px; margin: 50px auto; background: white; padding: 30px; border-radius: 10px; }
        form label { display: block; margin-top: 15px; }
        form input, form textarea { width: 100%; padding: 8px; margin-top: 5px; }
        button { margin-top: 20px; padding: 10px 15px; background: #007bff; color: white; border: none; border-radius: 4px; }
        button:hover { background: #0056b3; }
        a { text-decoration: none; color: #007bff; }
    </style>
</head>
<body>
<div class="container">
    <h1>{{ action }} Post</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }} <!-- Renders form fields with <p> tags -->
        <button type="submit">{{ action }}</button>
    </form>
    <br>
    <a href="{% url 'home' %}">Back to home</a>
</div>
</body>
</html>
```


![image](https://github.com/user-attachments/assets/c54003b8-29b1-400c-a1f5-23a6343740c3)


---

### `templates/post_confirm_delete.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Delete Post</title>
    <style>
        body { font-family: sans-serif; background: #f5f5f5; }
        .container { max-width: 600px; margin: 100px auto; background: white; padding: 30px; border-radius: 10px; text-align: center; }
        button { margin-top: 20px; padding: 10px 15px; background: #dc3545; color: white; border: none; border-radius: 4px; }
        button:hover { background: #c82333; }
        a { display: block; margin-top: 20px; color: #007bff; }
    </style>
</head>
<body>
<div class="container">
    <h2>Are you sure you want to delete this post?</h2>
    <p><strong>{{ post.title }}</strong></p>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Yes, Delete</button>
    </form>
    <a href="{% url 'home' %}">Cancel</a>
</div>
</body>
</html>
```


![image](https://github.com/user-attachments/assets/e7c1ec7b-da07-42a0-bfde-32f1ee8bfc2e)



---

## 5. Git Commands(additional)

```bash
git add .
git commit -m "Add create, edit, delete functionality with custom forms and templates"
git push
```
---
