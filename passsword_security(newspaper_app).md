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

