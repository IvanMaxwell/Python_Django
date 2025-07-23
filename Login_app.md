###  Features:

* User Signup (Registration)
* User Login
* User Logout
* Homepage (only accessible after login)
* Bootstrap-styled templates (optional)

---

###  Project Structure

We’ll create:

```
login_project/
├── accounts/         ← App for handling user login/logout
│   ├── templates/
│   │   └── accounts/
│   │       ├── login.html
│   │       ├── signup.html
│   │       └── home.html
├── login_project/    ← Django project config
└── manage.py
```

---

### 🔨 Step-by-step Instructions

#### 1. Create the Django Project & App

```bash
django-admin startproject login_project
cd login_project
python manage.py startapp accounts
```

#### 2. Update `settings.py`

```python
# login_project/settings.py

INSTALLED_APPS = [
    ...
    'accounts',
    'django.contrib.staticfiles',  # ensure this is present
]

# Add this for login redirect
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'
```

---

#### 3. Define URLs

##### `login_project/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
```

##### `accounts/urls.py`:

```python
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```

---

#### 4. Create Views

##### `accounts/views.py`:

python
```
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'accounts/home.html')
```

---

#### 5. Create Templates

##### `accounts/templates/accounts/signup.html`

<!DOCTYPE html>
<html>
<head>
    <title>Sign Up</title>
    <style>
        body {
            background-color: #f2f2f2;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 40px;
        }
        form {
            display: inline-block;
            margin-top: 20px;
            text-align: left;
        }
        button {
            margin-top: 10px;
            padding: 10px 20px;
            background-color: #17a2b8;
            border: none;
            color: white;
            border-radius: 5px;
        }
        button:hover {
            background-color: #138496;
        }
        a {
            display: block;
            margin-top: 15px;
            color: #007BFF;
        }
    </style>
</head>
<body>
    <h2>Sign Up</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Register</button>
    </form>
    <a href="{% url 'login' %}">Already have an account? Login here</a>
</body>
</html>
```

---

##### `accounts/templates/accounts/login.html`

```
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        body {
            background-color: #f2f2f2;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 40px;
        }
        form {
            display: inline-block;
            margin-top: 20px;
            text-align: left;
        }
        button {
            margin-top: 10px;
            padding: 10px 20px;
            background-color: #28a745;
            border: none;
            color: white;
            border-radius: 5px;
        }
        button:hover {
            background-color: #218838;
        }
        a {
            display: block;
            margin-top: 15px;
            color: #007BFF;
        }
    </style>
</head>
<body>
    <h2>Login</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Login</button>
    </form>
    <a href="{% url 'signup' %}">Don't have an account? Sign up here</a>
</body>
</html>
```

---

##### `accounts/templates/accounts/home.html`

```
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
    <style>
        body {
            background-color: #f2f2f2;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 40px;
        }
        h2 {
            color: #333;
        }
        a {
            display: inline-block;
            text-decoration: none;
            color: white;
            background-color: #007BFF;
            padding: 10px 20px;
            border-radius: 5px;
        }
        a:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h2>Welcome {{ request.user.username }}</h2>
    <p>This is your home page</p>
    <a href="{% url 'logout' %}">Logout</a>
</body>
</html>
```

---

#### 6. Run Migrations and Start Server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

###  You’re Done!

Now visit:

* `http://127.0.0.1:8000/signup/` → to create an account
* `http://127.0.0.1:8000/login/` → to log in
* After logging in, you'll be redirected to the home page.
* Click Logout to log out and return to login page.

---
