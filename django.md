# chapter0: Coding 101


---

#  The World of IT 

## 1.  What Is IT (Information Technology)?

* IT means using computers and software to store, process, and share information.
* Everything you do on a phone, laptop, or the internet is powered by IT.
* IT builds apps like YouTube, banking websites, online shopping, and even school portals using a skill called coding.

🪄 **In Simple Words**: IT is like the magic that makes computers, phones, and websites work together to do cool things.

---

## 1.  What Is Coding?

* **Coding** means giving instructions to a computer to do something.
* These instructions are written in a **programming language** (like Python, HTML, JavaScript).
* Computers **can’t think**, they only follow what we write — step by step.

🪄 **In Simple Words**: Coding is like writing a recipe for the computer to follow.

---

## 2.  How Does Coding Work?

* You write **code** (the instructions) in a text editor.
* The computer **reads** the code line-by-line and does what you tell it.
* If there's a **mistake** (called a bug), it tells you so you can fix it.

 Example:

```python
print("Hello, world!")  # This tells the computer to show a message
```

🪄 **In Simple Words**: You tell the computer what to do, and it does it exactly the way you say.

---


# Introduction to Python and Django

*Beginner-Friendly with Simple Explanations*

---

## Part 1: What Is Python?

### Technical Explanation

Python is a high-level programming language used to create software. It is known for its clean, easy-to-read syntax and is widely used for building websites, automating tasks, analyzing data, developing AI models, and more. Python lets you write instructions that a computer can understand and follow.

### Why Python?

* The code is simple and looks like English.
* It doesn't require deep technical knowledge to get started.
* It works across many fields: web development, automation, data science, etc.
* Python is a way to talk to your computer.
* It’s like giving step-by-step instructions to a robot. You say what you want, and it does it exactly how you wrote it.
* You don’t need to know everything—just learn how to give good, clear instructions.

### Example Code

```python
print("Welcome to Python")
```

This command tells the computer to display the message "Welcome to Python" on the screen.
---

## What is a Framework?

A **framework** is a **pre-built set of tools and rules** that makes your coding work faster and easier.
Instead of writing everything from scratch, you can use a framework to handle common things like:

* Making web pages
* Connecting to databases
* Handling forms and logins

### Simple Example:

Imagine you want to build a house.

Without a framework → You cut wood, mix cement, build walls—all by hand.
With a framework → You get pre-made walls, doors, windows—you just put them together.

---

## Why Use a Framework with Python?

Python is powerful by itself, but frameworks:

* Save you **time and effort**
* Help you build **bigger projects** easily
* Organize your code better
* Come with built-in features (like login systems, admin panels, security)

---

##  Python Frameworks (and What They’re Used For)
Here’s a **simple visual-style chart** (text-based) that shows **which Python framework to use for what type of project**, designed to be **print-friendly and beginner-friendly**.

---

# Python Frameworks at a Glance

| Project Type              | Recommended Framework | Description                                          |
| ------------------------- | --------------------- | ---------------------------------------------------- |
| **Websites**              | Django                | Full-featured, includes login, database, admin       |
|                           | Flask                 | Simple and flexible, great for small apps            |
|                           | FastAPI               | Fast and modern, ideal for APIs and microservices    |
| **Desktop Apps**          | Tkinter               | Built-in GUI toolkit, easy for beginners             |
|                           | PyQt / Kivy           | Advanced interfaces, touch and gesture support       |
| **Mobile Apps**           | Kivy                  | Cross-platform, supports mobile UIs                  |
| **Games**                 | Pygame                | 2D game development with sound and images            |
| **AI / Machine Learning** | TensorFlow / PyTorch  | Used for deep learning, image and speech recognition |
| **Data Projects**         | Pandas (Library)      | Not a framework, but used for data analysis          |
|                           | Jupyter Notebooks     | Interactive coding environment for data & visuals    |


---



##  What Is Django?

###  Explanation

Django is a web framework built using Python. A framework is a collection of tools that makes it faster and easier to build websites. Django handles many tasks like connecting to a database, showing web pages, creating login systems, and managing data—all with less code and more structure.Django is like a ready-made website builder kit made with Python. Imagine you want to build a LEGO house. Python is your hands and brain. Django is the full LEGO kit—it already has doors, windows, and roof parts ready for you. You just arrange them to build your house. we will see more about this in next topic 

---

## How Python and Django Work Together

### Technical Explanation

When you create a web application with Django, you write the logic in Python. Django uses your Python code to handle browser requests, display pages, save and update data in a database, and handle user accounts. Python gives the instructions, and Django organizes and runs them in a web environment.

### Example Use Case

Let’s say you want to create a to-do list web app:

* Use Python to define what a "task" is and how it behaves.
* Use Django to show a form to enter tasks, save them to a database, and display them on the website.

### Simple Explanation

Think of Python like writing the recipe for a cake. Django is the kitchen with tools that help you bake it. You bring the steps (Python), Django handles the oven, the ingredients, and the table to serve the cake. Together, they help you build something that works and looks nice.

---

## Summary

| Term     | Meaning                                                                                                      |
| -------- | ------------------------------------------------------------------------------------------------------------ |
| Python   | A simple language to write computer instructions                                                             |
| Django   | A framework built with Python to help you build websites                                                     |
| Together | They allow you to create web applications, like to-do lists, blogs, or login systems, easily and efficiently |

---

# Chapter 1:  Django:   // Under-development

# Introduction to django
* Django is a high-level Python web framework that allows rapid development of secure and maintainable websites.
* 2003: Created by developers at the Lawrence Journal-World newspaper to manage news content.
* 2005: Open-sourced and named after jazz guitarist Django Reinhardt.
* It follows the MVT (Model-View-Template) architectural pattern.
* Django comes with built-in tools for most of the coding tasks such like routing, templating, authentication, admin, and ORM database management.
* Imagine building a website like stacking blocks — Django gives you most of the blocks already shaped and ready to place.
* It's like a recipe book that not only gives the recipe but also the ingredients and tools to cook with.
* **Example:**

  ```bash
  django-admin startproject mysite
  ```

  This command starts a new Django project named `mysite`.
* **Example:**

  ```bash
  python manage.py runserver
  ```

  This runs a development server so you can view the site in your browser.


  ---


## django vs flask


* **Django**: Comes with everything built-in (admin panel, user login, database tools). Best for full-featured apps and bigger projects. Great for beginners who want structure.Its more useful for complex and bigger app 

* **Flask**: Very minimal at the start. You add features yourself. Best for small or custom apps. Gives you more flexibility, but you have to manage more on your own.Flaks is simple used for smaller apps and mostly for tasks

---

Use **Django** if you want to build fast with lots of features already provided.
Use **Flask** if you want full control and are okay building things piece by piece.




## Django Project

* A Django project is the main folder that contains your website’s full configuration.
* It includes files like `settings.py`, `urls.py`, `wsgi.py`, and `asgi.py`.
* A single project can contain many apps that work together to create one site.
* The project defines global settings and acts as the central controller of the application.

---

## Django App

* An app is a component of a project that performs a specific function (like a blog or login system).
* Apps help in organizing code into smaller, manageable parts.
* Multiple apps can be used inside one project.
* Each app includes its own views, models, templates, and URL configurations.

---

## MVT Pattern (Model–View–Template)

* Django follows the MVT architectural pattern to separate concerns in code.
* The Model handles data and database operations.
* The View processes requests and returns responses.
* The Template handles how data is displayed in HTML to the user.

<img width="332" height="152" alt="mvt in djnago" src="https://github.com/user-attachments/assets/f332ac49-d394-4b7d-a215-13a98f4e0276" />

---

## Models

* Models define the structure of the data in the database using Python classes.
* Each model class corresponds to a table in the database.
* Django’s ORM uses these models to automatically create and manage database tables.
* Fields in a model represent columns in the table (like text or date).

---

## Views

* Views process user requests and return appropriate responses.
* They are the connection between the models (data) and templates (UI).
* Views can be written as functions or classes.
* They determine what data is shown and how the user interacts with it.

---

## Templates

* Templates are HTML files used to display data to the user.
* They use Django’s templating syntax to include dynamic data in HTML.
* Templates keep the presentation logic separate from business logic.
* Template tags and filters are used to handle conditions and loops.

---

## URLs and URL Dispatcher

* The URL dispatcher maps browser requests (URLs) to views in Django.
* Defined in `urls.py`, each path is connected to a view function or class.
* `include()` is used to organize app-level URLs.
* It allows for clean and maintainable routing logic.

  <img width="1200" height="628" alt="image" src="https://github.com/user-attachments/assets/687959a4-f731-4f49-9482-9ae29065f346" />


---

## Django ORM 

* ORM stands for Object-Relational Mapping.
* It allows you to interact with the database using simple Python code instead of writing SQL manually.
* You can create, read, update, and delete data by calling Python methods.
* The ORM connects your Django models to actual database records.
* It makes database work easier and less error-prone for beginners.

---

## Migrations

* Migrations are files Django creates to apply changes in models to the actual database.
* Use `makemigrations` to create migration files and `migrate` to apply them.
* They track and apply changes like new fields or tables.
* Migrations help keep your database and code in sync.

---

## Forms

* Forms in Django collect and validate user input.
* `Form` handles custom fields, while `ModelForm` connects directly to a model.
* Django forms help prevent invalid or malicious data from being submitted.
* They support clean data validation and user-friendly error handling.

---

## Admin Interface

* Django provides a built-in admin panel to manage data models through a browser.
* It allows developers and site owners to add, edit, or delete data quickly.
* Models must be registered to appear in the admin.
* The admin panel is customizable and useful for non-developers too.

---

## Authentication

* Django includes built-in tools for user login, logout, and password management.
* It supports sessions, groups, and permissions for controlling access.
* The default `User` model can be customized or replaced.
* Authentication is secure by default and works out of the box.

---

## Static Files and Media

* Static files are CSS, JavaScript, and images used in the frontend.
* Media files are user-uploaded files like photos and documents.
* Django uses separate folders and URLs for static and media files.
* You must configure `STATIC_URL` and `MEDIA_URL` in your settings.

---

## Middleware

* Middleware is a set of functions that run before or after each request or response.
* They perform common tasks like authentication, security, and session handling.
* Middleware is defined in the `MIDDLEWARE` setting as a list.
* They can be custom-written or use Django’s built-in options.

---

## Django Shell

* The Django shell is a command-line tool to test and run Django code interactively.
* Run it using `python manage.py shell`.
* It loads all models and project settings automatically.
* Great for testing queries and understanding how models work.

---


# Django Built-in Features

## 1. Admin Interface

* Django includes a built-in admin panel to manage database models.
* It is auto-generated from models you define and is ready to use after login.
* Site admins can add, edit, and delete data without touching code.
* You register models using `admin.py` to make them available in the admin.

---

## 2. Authentication System

* Django has a complete authentication system with login, logout, and password handling.
* It provides secure session management and password hashing.
* User permissions and group-based access control are built in.
* You can customize the User model or extend it to add new fields.

---

## 3. ORM (Object-Relational Mapper)

* Django’s ORM lets you use Python code to work with databases instead of SQL.
* You can create, read, update, and delete records using model methods.
* It keeps your Python code and the database tightly linked.
* ORM makes working with databases safer and easier to understand.

---

## 4. URL Routing System

* Django routes incoming web requests (URLs) to specific views using `urls.py`.
* It uses `path()` and `re_path()` for clean and readable URL mapping.
* Apps can have their own `urls.py` and be included in the main project.
* This separation keeps your app modular and maintainable.

---

## 5. Templating Engine

* Django’s template engine lets you build dynamic HTML pages.
* It separates the presentation layer from Python logic.
* You use template tags and filters to display data, loop through content, or apply logic.
* Templates are stored in a `templates` folder within the app or project.

---

## 6. Middleware Support

* Middleware are small programs that run between the request and response cycles.
* They can handle tasks like security, sessions, or content modification.
* Django includes useful middleware by default, like CSRF protection and user auth.
* You can write your own middleware or remove/replace the defaults.

---

## 7. Forms and ModelForms

* Django includes a robust system to handle forms and user input.
* Forms handle validation and rendering HTML inputs easily.
* `ModelForm` connects a form directly to a database model.
* This reduces repetition and ensures clean data storage.

---

## 8. Sessions

* Django can store user session data across requests.
* It supports server-side sessions using the database or file storage.
* Sessions help maintain user state like login info or shopping carts.
* All of this works without exposing sensitive data to the browser.

---

## 9. Messages Framework

* Django allows temporary messages (e.g. “Post created successfully”) to be stored and shown to users.
* These messages are stored during one request and displayed on the next page.
* You can assign message levels like info, success, warning, or error.
* Messages improve the user experience and communication.

---

## 10. Static Files Handling

* Django supports serving static files like CSS, JS, and images during development.
* You define a `STATIC_URL` and collect all static files in one directory.
* In production, static files are served via a dedicated server (e.g., NGINX).
* The `collectstatic` command prepares files for deployment.

---

## 11. CSRF Protection

* Django provides built-in protection against Cross Site Request Forgery attacks.
* It adds a CSRF token to all forms and checks it before processing requests.
* This ensures form data is submitted by legitimate users.
* You can use `{% csrf_token %}` in templates to enable protection.

---

## 12. Internationalization (i18n)

* Django supports translation and formatting for multiple languages and locales.
* It helps build applications that can serve users around the world.
* You can mark text for translation and use different locale settings.
* Built-in tools help manage translation files and language switching.

---

## 13. Error Handling and Debugging Tools

* Django shows detailed error pages in development with stack traces and hints.
* You can customize 404, 500, and other error pages.
* Settings like `DEBUG=True` help while building, and should be `False` in production.
* It’s designed to help you catch and fix bugs quickly and clearly.

---




# Chapter 1: Initial Set Up of Django   


 
 - This chapter covers how to properly configure your computer to work on Django projects.
 
 - We start with an overview of the command line and how to install the latest version of Django and Python.
 
 - Then we discuss virtual environments, git, and working with a text editor.
 
 - By the end of this chapter you’ll be ready to create and modify new Django projects in just a few keystrokes.

 - Before we explore about Django we need to know about some general inforamation,
---
 # Command line in django

**Using the Command Line:**

- The command line is essential for Django development, used for setting up and managing projects.

**To Open the Command Line follow these steps,**
 
 
Mac: Open Terminal from

Applications > Utilities > Terminal


Windows: Open Terminal using

Use PowerShell (recommended over Command Prompt) or use git bash 

**Note: vs code has default terminal build-in connected with powershell**

![image](https://github.com/user-attachments/assets/8d72b467-d777-49ba-b07e-00f2e064bde1)

---

| Command      | Description                 |
| ------------ | --------------------------- |
| `cd`         | Navigate into a directory   |
| `cd ..`      | Move up one directory       |
| `ls` / `dir` | List files (Mac / Windows)  |
| `pwd`        | Show current directory path |
| `mkdir`      | Create a new directory      |
| `touch`      | Create a new file on mac      |


---

# How to install django:

**Installing Python**

Python is required for Django development.

Follow the steps below to install it on your system.

---

**For macOS**
Check if Python is installed:

terminal
```
python3 --version
```

If not installed, use Homebrew:

terminal
```
brew install python
```
---
**For Windows,**

Download Python from the official site:

https://www.python.org/downloads/windows/

Run the installer:

Make sure to check the box that says "Add Python to PATH"

Note:If the python isn't working check out this website for guide,https://realpython.com/installing-python/

---

**For Linux**

Use your package manager. Example for Debian/Ubuntu:

terminal
```
sudo apt update  
sudo apt install python3 python3-pip
```

Verify Installation
Run the following in your terminal or PowerShell:

terminal
```
python3 --version
pip3 --version
```
If you see version numbers, Python and pip are successfully installed.

---


# installation of django

 
**1. Make sure Python is already installed in our system for django**
 terminal
```
python --version 
 ```
---
**3. Install django by using pip**

**Command:**
terminal
``` 
pip install django 
```

The temrinal will show you the following in proccces of insatllation,

![image](https://github.com/user-attachments/assets/3edeb66f-d541-4cf8-b973-2646262fd218)

---

**3. To check django version:** 
 terminal
 ```
py -m django --version
```

---

# Virutual environment

**Using Virtual Environments**

Virtual environments are isolated containers that hold the dependencies for a specific Python project.

This prevents conflicts between projects using different package versions 

---

**Why Use Virtual Environments?**

- Keeps project dependencies separate

- Avoids version conflicts

- Ensures consistent environments across systems

- Standard practice in Python development

---

**Note:**

- In python we have a  built-in Python module used to create isolated virtual environments

- we also have a  third-party tool called pipenv that combines virtual environment management and package management into a single workflow.


---

**Example Workflows**

| Platform    | Create Environment      | Activate Environment        |
| ----------- | ----------------------- | --------------------------- |
| Windows     | `python -m venv .venv`  | `.venv\Scripts\activate`    |
| macOS/Linux | `python3 -m venv .venv` | `source .venv/bin/activate` |

---

**basic of venv:**

terminal

- python -m venv .venv            # Create environment
- .venv\Scripts\activate          # Activate on Windows
- source .venv/bin/activate       # Activate on macOS/Linux
- pip install django              # Manually install packages
- pip freeze > requirements.txt   # Save dependencies



---


# Installation of GIT


### What is Git?

**Git** is a **version control system** used to track changes in code, collaborate with other developers, and revert to earlier versions of a project when needed.

It works similarly to “track changes” in Microsoft Word or Google Docs, but is built specifically for software development.

* [Official Git Website](https://git-scm.com/)
* [What is Version Control? (Wikipedia)](https://en.wikipedia.org/wiki/Version_control)

---

### Install Git

#### On macOS

**Terminal:**

```terminal
brew install git
```

**Why:**
This command uses **Homebrew**, a macOS package manager, to download and install Git. It’s the recommended way for Mac users.

---

#### On Windows

1. Visit [Git for Windows](https://gitforwindows.org/)
2. Click the **Download** button
3. Follow the installation prompts

**Why:**
This provides Git along with Git Bash (a command-line tool), which allows you to use Git commands on Windows easily.

---

### Configure Git (One-Time Setup)

After installation, you need to tell Git your name and email address. This information will be attached to your commits.

**Terminal:**

```terminal
git config --global user.name "Your Name"
git config --global user.email "yourname@email.com"
```

**Why:**
Git uses this information to record who made each change. You can update it anytime using the same commands.

---

### Verify the Installation

**Terminal:**

```terminal
git --version
```

**Why:**
This checks if Git is correctly installed and displays the version number.

---

### Common Use Cases for Git

* Initialize and manage local repositories
* Commit and track file changes
* Collaborate via GitHub, GitLab, etc.
* Safely branch and merge features or fixes

---

### Text Editors
 
The final step is our text editor. While the command line is where we execute commands for our programs, a text editor is where the actual code is written. 
 
The computer doesn’t care what text editor you use–the end result is just code–but a good text editor can provide helpful hints and catch typos for you.
 
 Experienced developers often prefer using either Vim27 or Emacs28, both decades-old, text-only
 editors with loyal followings.
 
 However each has a steep learning curve and requires memorizing many different keystroke combinations. I don’t recommend them for newcomers 

 
 Modern text editors combine the same powerful features with an appealing visual interface.
 
 My current favorite is Visual Studio Code29 which is free, easy to install, and enjoys widespread
 popularity.
 
 If you’re not already using a text editor, download and install Visual Studio Code30
 now.
 
---

# Chapter2: Hello World App

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





# Chapter 2: Pages App

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


# Chapter 3: Message Board App with Django Admin

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

# Chapter 4: Django Blog App  // (needs to be recreated)

This guide builds a basic blog app in Django that:

* Lists all blog posts on the homepage
* Has a clean UI using inline CSS
* Does not include user login, registration, or post creation via form
* we will add new features in upcoming lessons

---

## 1. Set up the project

bash

```
# Create project folder
mkdir django-blog
cd django-blog


# Create a Django project
django-admin startproject myblog .

# Create a blog app
python manage.py startapp blog
```
## Then create templates into the django-blog

---

## 2. Update settings.py

Open `myblog/settings.py` and make the following changes:

### Add the blog app to installed apps

python

```
INSTALLED_APPS = [
    ...
    'blog',  # Enables the blog app
]
```

### Configure templates directory

```python
import os  # Required for BASE_DIR path handling

TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Adds global templates folder
        'APP_DIRS': True,  # Enables app-specific templates
        ...
    },
]
```

---

## 3. Define the BlogPost model

In `blog/models.py


python

```
from django.db import models  # Import Django's model module

class BlogPost(models.Model):  # Defines the blog post model
    title = models.CharField(max_length=200)  # Title of the post
    content = models.TextField()  # Content of the post
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.title  # Display post title in admin
```

### Make and apply migrations

bash

```
python manage.py makemigrations
python manage.py migrate
```

---

## 4. Create a view

In `blog/views.py`:

python

```
from django.shortcuts import render  # Imports render shortcut
from .models import BlogPost  # Imports the BlogPost model

def home(request):
    posts = BlogPost.objects.all()  # Fetch all blog posts
    return render(request, 'home.html', {'posts': posts})  # Render template with posts
```

---

## 5. Configure URLs

### In `myblog/urls.py`:

python

```
from django.contrib import admin
from django.urls import path
from blog.views import home  # Import home view

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('', home, name='home'),  # Home page route
]
```

---

## 6. Create the template

### Create folder:

```
django-blog/
└── templates/
    └── home.html
```

### Create `home.html`:

html
```

{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>My Blog</title>
    <style>
        /* Inline CSS to style the page */
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            color: #333;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 800px;
            margin: 40px auto;
            background: white;
            padding: 20px 30px;
            border-radius: 8px;
            box-shadow: 0 5px 10px rgba(0,0,0,0.05);
        }

        h1 {
            text-align: center;
            margin-bottom: 20px;
            color: #444;
        }

        ul {
            list-style: none;
            padding: 0;
        }

        li {
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 1px solid #ddd;
        }

        li strong {
            display: block;
            font-size: 18px;
            margin-bottom: 5px;
            color: #0066cc;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>All Blog Posts</h1>
        <ul>
            {% for post in posts %}
                <li>
                    <strong>{{ post.title }}</strong> <!-- Post title -->
                    {{ post.content }} <!-- Post content -->
                </li>
            {% empty %}
                <li>No posts available.</li> <!-- Message if no posts -->
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```

---

## 7. Register model in admin

In `blog/admin.py`:

python

```
from django.contrib import admin
from .models import BlogPost  # Import the BlogPost model

admin.site.register(BlogPost)  # Register model with Django admin
```

Create a superuser to log in:

bash

```
python manage.py createsuperuser
```
<img width="1378" height="404" alt="image" src="https://github.com/user-attachments/assets/5cf317d1-51dc-43c8-bb05-3cd21cf46594" />

---

## 8. Run the server


## before you run the server check if the structure of your directory matches this following image,

![image](https://github.com/user-attachments/assets/97ac74e2-4d04-4257-83f8-5f22a2f1f3a5)


bash

```
python manage.py runserver
```

Visit:

* [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see your homepage
* [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) to add posts




---

## 9. Optional: Create `.gitignore`

Create a `.gitignore` file in the root directory:

gitignore

```
venv/
__pycache__/
*.pyc
*.sqlite3
.env
```

---

## 10. Push to GitHub (additional)

```bash
git init
git add .
git commit -m "Initial Django blog setup with inline CSS"
git remote add origin https://github.com/yourusername/django-blog.git
git push -u origin main
```

---

![image](https://github.com/user-attachments/assets/ba5f3f73-d755-4104-b774-d97989784f0d)



# Chapter 5: Forms in django


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

# Chapter 6: Ariticle app


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

<img width="2140" height="727" alt="image" src="https://github.com/user-attachments/assets/15688369-d848-469f-91e5-fe34536fc390" />


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
<img width="1883" height="1003" alt="image" src="https://github.com/user-attachments/assets/36801908-748d-4c12-9b9f-f00c0e0a5b9c" />


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

<img width="568" height="1192" alt="image" src="https://github.com/user-attachments/assets/4fbef58a-dd1a-494d-9227-368dde13b9bc" />

---

#  Chapter 7: User Authentication and password management

- To learn about basic authentication system  we'll integrate the following into our blog app:

* **User Login**
* **User Logout**
* **User signup**
  

---

## 1. Update `settings.py`

Add this to the **bottom** of `myblog/settings.py`:

python
```
# Redirect after login/logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

---

##  2. Add Auth URLs to Main `urls.py`

In `myblog/urls.py`, import Django’s auth views and add paths:

python
```

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

```

---

## 3. Add Registration URL
In blog/urls.py:

python
```
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('add/', views.create_post, name='create-post'),
    path('register/', views.register, name='register'),
]

```

---

##  4. Protect "Add Post" View (Login Required)

Update view in `blog/views.py` to require login and signup:

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


##  5. Create a Registration Form
In blog/forms.py, add a registration form using Django's built-in UserCreationForm:

 ```
from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

 ```


##  6. Show Login/Logout and signup in Navbar 

Update `blog/templates/blog/home.html` to show login/logout and signup:
html
```
<!DOCTYPE html>
<html>
<head>
    <title>Blog Home</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f9f9f9;
            
        }

        h1 {
            color: #333;
            margin-bottom: 20px;
        }

        .post {
            background: #fff;
            border: 1px solid #ddd;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
        }

        .post h2 {
            margin: 0;
            color: #2c3e50;
        }

        .post small {
            color: #888;
        }

        a.button {
            display: inline-block;
            padding: 10px 15px;
            background-color: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin-bottom: 20px;
        }

        a.button:hover {
            background-color: #0056b3;
        }


    </style>
</head>
<body>
        <h1>Blog Posts</h1>

   {% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}! 
    <form method="post" action="{% url 'logout' %}">
    {% csrf_token %}
    <button type="submit">Logout</button>
    </form>
{% else %}
    <a href="{% url 'login' %}" class="button">Login</a><br>
    <a href="{% url 'register' %}" class="button" style="background-color: #4947a8;">Register</a>
    
{% endif %}

    <hr>
    
    {% for post in posts %}
        <div class="post">
            <h2>{{ post.title }}</h2>
            <p>{{ post.content }}</p>
            <small>By {{ post.author }} on {{ post.date_posted }}</small>
        </div>
    {% empty %}
        <p>No posts yet.</p>
    {% endfor %}
</body>
</html>

```

---
---
##  3. Create Login Template

**Path:** `blog/templates/blog/login.html`

html
```
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f4f4;
        }

        form {
            background: #fff;
            padding: 25px;
            border: 1px solid #ddd;
            border-radius: 8px;
            max-width: 400px;
        }

        button {
            padding: 10px 15px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
        }

        a {
            margin-top: 15px;
            display: inline-block;
        }
    </style>
</head>
<body>
    <h1>Login</h1>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Log in</button>
    </form>
</body>
</html>
```
---

## 6. Create a sign up templates:

```
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f4f4;
        }

        form {
            background: #fff;
            padding: 25px;
            border: 1px solid #ddd;
            border-radius: 8px;
            max-width: 400px;
        }

        button {
            padding: 10px 15px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 4px;
        }

        a {
            margin-top: 15px;
            display: inline-block;
        }
    </style>
</head>
<body>
    <h1>Register</h1>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Sign Up</button>
    </form>

    <a href="{% url 'login' %}">Already have an account? Log in</a><br>
    <a href="{% url 'blog-home' %}">← Back to Home</a>
</body>
</html>

```

---
##  6. Create a User to Test
bash
```
python manage.py createsuperuser
```
try and test the webpage you have created

##  Structure of blog app after adding all the above given features

![image](https://github.com/user-attachments/assets/03f6cad0-50f4-46c2-86cf-519a6aff12be)

 ---


## To learn about more clear flow of authentication and password management we will intergerate the following features into a sperate app 'accounts' .All using custom templates/pages, not the default Django ones,

* **User signup**
* **Login**
* **Logout**
* **Password change**
* **Password reset**




## Note:This app is just to teach you the flow of authentication and accounts , it does not include real security features this is only for beginner level learning

---

##  Step 1: Project Setup

### 1.1 Ensure your app is ready

If you haven’t created the app:

bash

```
python manage.py startapp accounts
```

### 1.2 Add `accounts` to `INSTALLED_APPS` in `settings.py`:

python

```
INSTALLED_APPS = [
    ...
    'accounts',
    'django.contrib.auth',
    'django.contrib.messages',
    ...
]
```

### 1.3 Configure `TEMPLATES` and `STATICFILES_DIRS` if needed:

Ensure your `TEMPLATES` setting looks like this:

python

```
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],  # global templates dir
        ...
    },
]
```

---

##  Step 2: Create URLs

### 2.1 In `accounts/urls.py`:

python

```
from django.urls import path
from . import views  
from django.contrib.auth import views as auth_views
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='base'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
     path('dashboard/', views.dashboard, name='dashboard'),
]
```

### 2.2 Include `accounts.urls` in your project’s `urls.py`:

python

```

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
```

---

##  Step 3: Create Signup View , homepageview and loginrequired

### 3.1 In `accounts/views.py`:

python

```

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Renders the homepage template
class HomePageView(TemplateView):
    template_name = 'base.html'

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')




```

---

##  Step 4: Create Templates



Note it has internal css

Create the following files in: `templates/accounts/`
(e.g., `myproject/templates/accounts/login.html`, etc.)

### 4.1 Base layout (`templates/base.html`)

html

```
<!DOCTYPE html>
<html>
<head>
     <title>Newspaper Auth</title>


        <style>
        /* General Page Styles */
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            margin: 0;
            padding: 0;
        }

        nav {
            background-color: #343a40;
            padding: 10px 20px;
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: flex-start;
        }

        nav form {
            margin: 0 5px;
        }

        nav button {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 8px 12px;
            cursor: pointer;
            border-radius: 4px;
            font-size: 14px;
        }

        nav button:hover {
            background-color: #0056b3;
        }

        hr {
            margin: 0;
            border: none;
            border-top: 1px solid #dee2e6;
        }

        .messages {
            padding: 15px;
            margin: 20px;
            background-color: #e9ecef;
            border-left: 5px solid #007bff;
            font-size: 14px;
        }

       
        main {
            padding: 20px;
        }

        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f1f3f5;
            margin: 0;
            padding: 0;
        }

        h2 {
            text-align: center;
            margin-top: 40px;
            color: #343a40;
        }

        form {
            max-width: 400px;
            margin: 30px auto;
            background: white;
            padding: 25px 30px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }

        form input[type="text"],
        form input[type="password"],
        form input[type="email"] {
            width: 100%;
            padding: 10px;
            margin: 8px 0 16px 0;
            border: 1px solid #ced4da;
            border-radius: 4px;
            font-size: 14px;
        }

        form button[type="submit"] {
            width: 100%;
            background-color: #007bff;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 4px;
            font-size: 15px;
            cursor: pointer;
        }

        form button[type="submit"]:hover {
            background-color: #0056b3;
        }

        .errorlist {
            color: #dc3545;
            list-style-type: none;
            padding-left: 0;
        }
    </style>
</head>



<body>
    <nav>
        <form method="post" action="{% url 'signup' %}">
    {% csrf_token %}
    <button type="submit">signup</button>
</form>
 |
        <form method="post" action="{% url 'login' %}">
    {% csrf_token %}
    <button type="submit">Login</button>
</form>
|
        <form method="post" action="{% url 'logout' %}">
        {% csrf_token %}
  
        <button type="submit">Logout</button>
        </form>|
        
        <form method="post" action="{% url 'password_change' %}">
    {% csrf_token %}
    <button type="submit">password change</button>
</form>
 |
<form method="post" action="{% url 'password_reset' %}">
    {% csrf_token %}
    <button type="submit">password reset</button>
</form>

     
    </nav>
    <hr>
    {% if messages %}
        {% for message in messages %}
            <p>{{ message }}</p>
        {% endfor %}
    {% endif %}
    {% block content %}{% endblock %}
</body>
</html>
```

### 4.2 Signup (`signup.html`)

html

```
{% extends "base.html" %}
{% block content %}
<h2>Sign Up</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign Up</button>
</form>
{% endblock %}
```

### 4.3 Login (`login.html`)

html

```
{% extends "base.html" %}
{% block content %}
<h2>Login</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
{% endblock %}
```

### 4.4 Logout (`logout.html`)

html

```
{% extends "base.html" %}
{% block content %}
<h2>You have been logged out.</h2>
<a href="{% url 'login' %}">Log in again</a>
{% endblock %}
```

### 4.5 Password Change & Done

**password\_change.html**

html

```
{% extends "base.html" %}
{% block content %}
<h2>Change Password</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Change</button>
</form>
{% endblock %}
```

**password\_change\_done.html**

html

```
{% extends "base.html" %}
{% block content %}
<p>Password changed successfully.</p>
{% endblock %}
```

### 4.6 Password Reset

**password\_reset.html**

html

```
{% extends "base.html" %}
{% block content %}
<h2>Reset Your Password</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Send Reset Email</button>
</form>
{% endblock %}
```

**password\_reset\_done.html**

html

```
{% extends "base.html" %}
{% block content %}
<p>Check your email for the reset link.</p>
{% endblock %}
```

**password\_reset\_confirm.html**

html

```
{% extends "base.html" %}
{% block content %}
<h2>Enter new password</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Change password</button>
</form>
{% endblock %}
```

**password\_reset\_complete.html**

html

```
{% extends "base.html" %}
{% block content %}
<p>Your password has been reset. <a href="{% url 'login' %}">Login</a></p>
{% endblock %}
```

**dashboard/./html**


html 
```
{% extends "base.html" %}

{% block title %}Dashboard{% endblock %}

{% block content %}
<div class="dashboard-container">
    <div class="dashboard-header">Welcome to Your Dashboard</div>

    <div class="dashboard-section">
        <h3>Your Profile</h3>
        <p>Name: {{ user.username }}</p>
        <p>Email: {{ user.email }}</p>
    </div>

    <div class="dashboard-section">
        <h3>Actions</h3>
        <a href="#" class="button">Update Profile</a>
        <a href="#" class="button">View Reports</a>
    </div>
</div>
{% endblock %}

```

---

## Step 5: Email Settings for Reset and Login Redirect

Add to `settings.py` (use console backend for dev):

python

```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = '/accounts/dashboard/'
```

---

## Step 6: Migrate , create a superuser & Run

bash

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/accounts/signup/` to start testing.

##  Structure of blog app after adding all the above given features



---



# Chapter 8 : Newspaper app ( full version )

This is a fully running news paper app combining all three app the accounts ,articles ,pages and config them with their repective templates , this can be easily considered a beginner level project in django


let's dive deep into django,




// guide needs to be checked



end of chapter,

Here is a task for you create a fully running blog app combining all three app the basic blog app ,forms in blog app and authentictaion of blog app and config them with their repective custom templates and try to improve the code quality 

refer to the 


# chapter 9: API

need to refered by sir



# chapter 10:deployement


