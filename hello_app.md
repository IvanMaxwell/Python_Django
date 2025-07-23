# Hello World App

 - In this chapter we’ll build a Django project that simply says “Hello, World” on the homepage.
   
 - This is the traditional way to start a new programming language or framework.

### Here step by step through **Chapter 2: Hello World App** for a Django project, covering:

1. Initial Setup
2. Create an App
3. URLs, Views, Models, Templates
4. Hello, World!
5. Git
6. Optional: GitHub and  SSH Key

I'll also give you a **structure** you can create manually, along with code and commands.

---

### Structure


![image](https://github.com/user-attachments/assets/4c1cac06-3d7c-4c4a-80d7-20126d2e5756)




###  1. Initial Setup

####  Install Django (if not already)

bash

```
pip install django
```

####  Start a Project

bash

```
django-admin startproject helloworld_project
cd helloworld_project
```

---

###  2. Create an App

bash

```
python manage.py startapp core
```

This creates a new Django app named `core`.

**Register the app in `settings.py`:**

python

```
# helloworld_project/settings.py
INSTALLED_APPS = [
    ...
    'core',
]
```

![image](https://github.com/user-attachments/assets/f8b56652-9022-4b1a-a531-6f96c3398e41)


---

### 3. URLs, Views, Models, Templates

#### Project-level URL setup:

python

```
# helloworld_project/urls.py
from django.contrib import admin
from django.urls import path path, include  #path:Lets you define URL patterns ,include: Lets you import URL patterns from another file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Link to app URLs
]
```

#### App-level URL setup:

Create `core/urls.py`:

python

```
# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
```

#### Views:

python

```
# core/views.py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")
```

---

### 4. Hello, World!

Run the development server:

bash

```
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) — you’ll see "Hello, World!"

![image](https://github.com/user-attachments/assets/286a0af8-41f1-4510-829c-b2d297951544)


---



### 5. Git

#### Initialize Git:

bash
```
git init
```

#### Create `.gitignore`:
- If you don't have a gitignore file ,then create it in your project root folder (e.g., HelloApp_Django), create a new file named: .gitignore

-  We can use this command in Powershell ,

```
  New-Item -Name ".gitignore" -ItemType "File"

```




bash
```
__pycache__/
*.pyc
db.sqlite3
.env
```



#### Add and Commit:

bash

```
git add .
git commit -m "Initial Hello World Django app"
```




---

###  Optional: 6. GitHub

#### Create a repo on [GitHub](https://github.com/new)

#### Link it:

bash

```

git remote add origin git@github.com:yourusername/helloworld-django.git
git push -u origin main
```

---
