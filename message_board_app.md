# Message Board App with Django Admin

-  In this chapter wewill use a database for the first time to build a basic Message Board application where users can post and read short messages.
-  We’ll explore Django’s powerful built-in admin interface which provides a visual way to make changes to our data.
-  A beginner-friendly Django application where users can post and read short messages.
-   We'll explore Django’s ORM, model-view-template architecture, and its powerful built-in admin interface.


### Additional: 

- Thanks to the powerful Django ORM (Object-Relational Mapper), there is built-in support for multiple database backends: PostgreSQL, MySQL, MariaDB, Oracle, or SQLite.

- This means that we, as developers, can write the same Python code in a models.py file and it will automatically be translated into each database correctly.

-  The only configuration required is to update the DATABASES64 section of our config/settings.py file.
  
-   This is truly an impressive feature, For localdevelopment,Django defaults to using SQLite65 because it is file-based and therefore far simpler to use than the other database options, which require a dedicated server to be running separate from Django itself.

---

#  Algorithm

1. Set up a new Django project.
2. Create a new app called `board`.
3. Define a `Message` model with `name`, `content`, and `timestamp`.
4. Register the model in `admin.py`.
5. Configure URL routing.
6. Create views to list and post messages.
7. Add templates for displaying and adding messages.
8. Use Django Admin to manage messages visually.
9. Test and run the server.

---

# Step-by-Step Guide

### 1. Initial Setup

bash

```
django-admin startproject messageboard_project           #start project
cd messageboard_project                                  
python manage.py startapp board                           #create app
```

Add `board` to `INSTALLED_APPS` in `settings.py`.

python

```
# messageboard_project/settings.py
INSTALLED_APPS = [
    ...
    'board',                                #Register app
]
```

---

### 2. Create the Message Model

python

```
# board/models.py
from django.db import models

class Message(models.Model):                               # Here is where we declare name,content,time
    name = models.CharField(max_length=50)                              # Name of the user
    content = models.TextField()                                         # The actual message
    timestamp = models.DateTimeField(auto_now_add=True)                # Auto-added time

    def __str__(self):
        return f"{self.name}: {self.content[:20]}"                     # First 20 chars as preview

```

### Run migrations:

bash

```
python manage.py makemigrations
python manage.py migrate
```

---

### 3. Enable Django Admin

Create a superuser:

bash

```
python manage.py createsuperuser           

```



Register the model:

python

```
# board/admin.py
from django.contrib import admin
from .models import Message

admin.site.register(Message)             #register the message
```

---

### 4. Create Views

python 

```
# board/views.py
from django.shortcuts import render, redirect
from .models import Message
from django.utils import timezone

def home(request):
z    messages = Message.objects.order_by('-timestamp')                  # Show latest first
    return render(request, 'board/home.html', {'messages': messages})

def post_message(request):
    if request.method == 'POST':                            #gets values from user
        name = request.POST['name']                         #gets the name of user and assign them
        content = request.POST['content']                   #gets the content from user and assign them
        Message.objects.create(name=name, content=content, timestamp=timezone.now())   #auto assign time of user's post
        return redirect('home')                             #return user to home page
    return render(request, 'board/post_message.html')        #add the user post
```

---

### 5. URLs

Create a `urls.py` in `board` app:

python

```
# board/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                             #url of home page in app
    path('post/', views.post_message, name='post_message'),        #url of post page in app         
]
```

Connect it to the project’s URL config:

python

```
# messageboard_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('board.urls')),                      #url of app
]
```

---

### 6. Templates

Create a folder `templates/board/` and add:

**home.html**

html

```
<!DOCTYPE html>
<html>
<head>
    <title>Message Board</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f4f8;
            margin: 0;
            padding: 40px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        h1 {
            color: #2c3e50;
            margin-bottom: 30px;
        }

        a {
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            text-decoration: none;
            border-radius: 6px;
            font-weight: bold;
            margin-bottom: 30px;
            display: inline-block;
            transition: background-color 0.3s ease;
        }

        a:hover {
            background-color: #2c80b4;
        }

        ul {
            list-style: none;
            padding: 0;
            max-width: 600px;
            width: 100%;
        }

        li {
            background-color: #fff;
            padding: 15px 20px;
            border-radius: 8px;
            margin-bottom: 12px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
            font-size: 16px;
        }

        li strong {
            color: #34495e;
        }

        li em {
            color: #888;
            font-size: 13px;
            margin-left: 8px;
        }
    </style>
</head>
<body>
    <h1>Message Board</h1>
    <a href="{% url 'post_message' %}">Post a Message</a>
    <ul>
      {% for msg in messages %}
        <li>
          <strong>{{ msg.name }}</strong>: {{ msg.content }}
          <em>({{ msg.timestamp }})</em>
        </li>
      {% empty %}
        <li>No messages yet.</li>
      {% endfor %}
    </ul>
</body>
</html>

```

![image](https://github.com/user-attachments/assets/c0e2356d-0e63-4581-9395-41f5df2e86f3)


**post\_message.html**

html

```
<!DOCTYPE html>
<html>
<head>
    <title>Post a Message</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f3f6fb;
            margin: 0;
            padding: 40px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .form-container {
            background-color: #ffffff;
            padding: 30px 40px;
            border-radius: 10px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 500px;
        }

        h1 {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 25px;
        }

        label {
            display: block;
            margin-top: 15px;
            margin-bottom: 5px;
            color: #333;
            font-weight: bold;
        }

        input[type="text"],
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 6px;
            box-sizing: border-box;
            resize: vertical;
            font-size: 14px;
        }

        textarea {
            min-height: 100px;
        }

        button {
            width: 100%;
            padding: 12px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 20px;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #2c80b4;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Post a Message</h1>
        <form method="post">
            {% csrf_token %}
            <label>Name:</label>
            <input type="text" name="name" required>

            <label>Message:</label>
            <textarea name="content" required></textarea>

            <button type="submit">Post</button>
        </form>
    </div>
</body>
</html>

```

![image](https://github.com/user-attachments/assets/bef95c03-42aa-41b3-8c07-273081cff962)


---

### 7. Run Server and Use Admin

bash

```
python manage.py runserver
```

* Visit `/` to see messages
* Visit `/post/` to add a message
* Visit `/admin/` to manage data with the superuser account

---

##  .gitignore

Create `.gitignore`:

gitignore

```
__pycache__/
*.pyc
db.sqlite3
.env
```


---

##  GitHub Steps

bash

```
git init
git add .
git commit -m "Initial commit for Message Board App"
gh repo create messageboard-app --public --source=. --remote=origin
git push -u origin main
```

---

# structure of code

![image](https://github.com/user-attachments/assets/d02d63c0-db9c-413a-ad7a-c017b97b33e4)



---
