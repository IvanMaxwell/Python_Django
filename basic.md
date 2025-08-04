# Chapter0: Introduction to Coding 



## The World of IT 

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

##  What Is Python?

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








# chapter 10:deployement


