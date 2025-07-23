# Pages App

- In this chapter we will build, test, and deploy a Pages app with a homepage and about page.
  
-  We’ll learn about Django’s class-based views and templates which are the building blocks for the more complex web applications built later on in the book.


Here’s a GitHub-friendly, chapter-style breakdown and explanation for building a **Django Pages App** with homepage and about page using class-based views and templates:

---

 Here's a **concise algorithm-style breakdown** of the Django Pages App project setup using class-based views and templates:


### **Algorithm: Build a Django Pages App**

1. **Start Project Setup**

   * Install Django using `pip`.
   * Create a Django project: `django-admin startproject pages_project`.

2. **Create Pages App**

   * Inside the project directory, run: `python manage.py startapp pages`.
   * Add `'pages'` to `INSTALLED_APPS` in `settings.py`.

3. **Configure URLs**

   * Create `pages/urls.py` with paths for homepage and about page.
   * Include `pages.urls` in the project's main `urls.py`.

4. **Create Views**

   * Use `TemplateView` to define `HomePageView` and `AboutPageView` in `views.py`.

5. **Create Templates**

   * Inside `pages/templates/`, create `home.html` and `about.html` with simple HTML headings.
   * Add inline css since we have only two pages

6. **Run the App**

   * Run `python manage.py runserver`.
   * Visit `http://127.0.0.1:8000/` for homepage and `/about/` for the about page.

7. **(Optional)Initialize Git**

   * Run `git init`.
   * Create `.gitignore` to exclude files like `__pycache__/`, `*.pyc`, `db.sqlite3`, `.env`.
   * Commit initial setup with `git add .` and `git commit -m "Initial commit"`.

8. **Push to GitHub**

   * Create a GitHub repository.
   * Add remote, rename default branch to `main`, and push code.

  
---

# Here is a step by step guide:

### 1. Initial Set Up



### Check django version

bash

```
python -m django --version 

```

**If version not shown**

**Install Django**

bash

```
pip install django
```


**Create a Django Project**

bash

```
django-admin startproject pages_project         #creates the project folder
cd pages_project                                 #directs to the folder
```

---

### 2. Create An App

**Create a new app called `pages`**

bash

```
python manage.py startapp pages                    #craetes an app inside project called page
```

**Add `'pages'` to `INSTALLED_APPS` in `pages_project/settings.py`**

python
```
INSTALLED_APPS = [
    ...
    'pages',                     #this important,if not give app will not be overlooked by compiler
]
```

![image](https://github.com/user-attachments/assets/1af94c0c-6e87-461b-9f36-20cfc999ef63)


---

### 3. URLs, Views, Models, Templates

**Create URL configurations**

In `pages/urls.py` (create this file):

python

```
from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),                                  #url for homepage
    path('about/', AboutPageView.as_view(), name='about'),                          #url for aboutpage
]
```

In `pages_project/urls.py`:

python

```
from django.contrib import admin
from django.urls import path, include                           #this is important or complier will not know about the include function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),                               #this will include the page url in pages_project's urls
]
```

---

### 4. Hello, World! (Class-based Views)

In `pages/views.py`:

python

```
from django.views.generic import TemplateView

# Renders the homepage template                    
class HomePageView(TemplateView):                     #function for homepage
    template_name = 'home.html'

# Renders the about page template
class AboutPageView(TemplateView):                    #function for aboutpage
    template_name = 'about.html'
```

---

### 5. Templates

Inside your app, create a folder: `pages/templates/`

Add `home.html`:

html

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Jeevi Times - Home</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #f4f7fa;
    }

    .container {
      max-width: 960px;
      margin: 50px auto;
      padding: 40px;
      background-color: #ffffff;
      border-radius: 12px;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.08);
      text-align: center;
    }

    h1 {
      color: #2c3e50;
      font-size: 36px;
      margin-bottom: 10px;
    }

    .subtitle {
      font-size: 18px;
      color: #555;
      margin-bottom: 30px;
    }

    .btn-group {
      margin-top: 30px;
    }

    .btn {
      display: inline-block;
      margin: 10px;
      padding: 12px 24px;
      background-color: #3498db;
      color: white;
      text-decoration: none;
      border-radius: 6px;
      font-weight: bold;
      transition: background-color 0.3s ease;
    }

    .btn:hover {
      background-color: #2c80b4;
    }

    .footer {
      margin-top: 40px;
      font-size: 14px;
      color: #999;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Welcome to Jeevi Times</h1>
    <p class="subtitle">
      Your daily source for news, opinions, and stories written by our community.
    </p>

    <div class="btn-group">
      <a href="/articles/" class="btn">Browse Articles</a>
      <a href="/articles/new/" class="btn">Write an Article</a>
      <a href="/about/" class="btn">About Us</a>
      <a href="/login/" class="btn">Login</a>
    </div>

    <div class="footer">
      &copy; 2025 Jeevi Times. Built with Django.
    </div>
  </div>
</body>
</html>

```

<img width="2434" height="1070" alt="image" src="https://github.com/user-attachments/assets/6130b7fd-4fc6-4d03-979d-e04f55c0b274" />


Add `about.html`:

html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About - Jeevi Times</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f7fa;
        }

        .container {
            max-width: 900px;
            margin: 60px auto;
            padding: 40px;
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
        }

        h1 {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 30px;
        }

        p {
            font-size: 17px;
            line-height: 1.6;
            color: #555;
            margin-bottom: 20px;
        }

        ul {
            margin-top: 10px;
            padding-left: 20px;
        }

        li {
            margin-bottom: 8px;
            color: #444;
        }

        .footer {
            margin-top: 40px;
            text-align: center;
            font-size: 14px;
            color: #888;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>About Jeevi Times</h1>
        <p>
            <strong>Jeevi Times</strong> is a simple, community-focused news platform built with Django.
            This project serves as a learning tool for beginners and a foundation for real-world Django applications.
        </p>
        <p>
            Our goals:
        </p>
        <ul>
            <li>Practice Django's template system and class-based views</li>
            <li>Implement CRUD functionality for articles</li>
            <li>Demonstrate user authentication and permission control</li>
            <li>Showcase modular design using Django best practices</li>
        </ul>
        <p>
            Whether you're here to read, write, or contribute — thank you for being part of Jeevi

```
<img width="2345" height="1007" alt="image" src="https://github.com/user-attachments/assets/96c0cccd-48ee-4061-8189-e305ccba5809" />



---

### 6. Git

**Initialize a Git repository**

bash

```
git init
```

**Create a `.gitignore` file**

bash

```
echo "__pycache__/
*.pyc
db.sqlite3
.env
" > .gitignore
```

**Add and commit**

bash

```
git add .
git commit -m "Initial commit"
```

---

### 7. Optional: GitHub

**Create a new repo on GitHub**, then:

bash

```
git remote add origin https://github.com/your-username/django-pages-app.git
git branch -M main
git push -u origin main
```


---
