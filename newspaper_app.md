# NewsPapaer_app // under development

To create the newspaper app we will pull the password security app (accounts app) we need to add the following things to the newspaper project with already add accounts app 

---

# 📄 Newspaper App – Full Guide (Text Version)

## 1. Project Structure

```
newspaper/
├── accounts/          # Signup & auth logic
├── articles/          # Article model and CRUD views
├── pages/             # Static pages: Home, About
├── newspaper/         # Project config: settings, urls
├── static/            # CSS and other assets
├── templates/         # Shared HTML templates
├── db.sqlite3         # Default SQLite DB
└── manage.py
```

---

## 2. Setup and Run the Project

bash

```
pip install django
cd newspaper
python manage.py runserver
```

Go to: `http://127.0.0.1:8000`

---

## 3. settings.py Configuration

In `newspaper/settings.py`, confirm:

python

```
INSTALLED_APPS = [
    ...
    'pages',
    'articles',
    'accounts',
]

TEMPLATES[0]['DIRS'] = [os.path.join(BASE_DIR, 'templates')]
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
```

---

## 4. Pages App (Home & About)

**pages/views.py**

python

```
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
```

**pages/urls.py**

python

```
from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]
```

---

## 5. Articles App (CRUD)

### Model

**articles/models.py**

python

```
from django.db import models
from django.conf import settings 
from django.contrib.auth import get_user_model
from django.db import models 
from django.urls import reverse

class article (models.Model):
    title = models.CharField(max_length=100)
    article= models.TextField()
    dateandtime = models.DateTimeField (auto_now_add=True)
    author=models.ForeignKey(get_user_model(),on_delete= models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail',args=[str(self.id)])
    



class Comment(models.Model):
    article = models.ForeignKey('article', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.article}'


```

---

### Views

**articles/views.py**

python

```
from django.views.generic import CreateView
from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,DeleteView,UpdateView
from .models import article 
from django.shortcuts import redirect
from .models import article, Comment
from .forms import CommentForm
# Create your views here.

class Articleslistview(ListView):
    model=article
    template_name='articles/articles_list.html'
    context_object_name='articles'




class Articlesdetailview(DetailView):
    model=article
    template_name='articles/article_detail.html'
    context_object_name='article'
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.save()
            return redirect('article_detail', pk=self.object.pk)
        return self.get(request, form=form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = kwargs.get('form') or CommentForm()
        context['comments'] = self.object.comments.all().order_by('-created_at')
        return context





class AritcleEditView(UpdateView):
    model=article
    fields=['title','article']
    template_name='articles/article_edit.html'





class AritcleDeleteView(DeleteView):
    model=article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('articles')







class ArticleCreateView(CreateView):
    model = article
    fields = ['title','article','author']  # match your model fields
    template_name = 'articles/articles_create.html'
    success_url = reverse_lazy('articles')
    
    

```

---

### URLs

**articles/urls.py**

python

```
from django.urls import path
from .views import (
    ArticleListView, ArticleDetailView,
    ArticleCreateView, ArticleUpdateView, ArticleDeleteView,
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
]
```

---

## 6. Accounts App (Signup)

### View

**accounts/views.py**

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

### URLs

**accounts/urls.py**

python

```
from django.urls import path
from . import views  
from django.contrib.auth import views as auth_views
from .views import HomePageView
from django.contrib.auth.views import LogoutView

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

---

## 7. Main Project URLs

**newspaper/urls.py**

python

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # built-in login/logout
    path('accounts/', include('accounts.urls')),              # custom signup
    path('articles/', include('articles.urls')),              # article views
    path('', include('pages.urls')),                          # home, about
]
```

---

## 8. Templates Folder Layout

```
yet to do it
```

Use `{% extends "base.html" %}` and `{% block content %}` to reuse layout.

---

## 9. Static Files

Static files like CSS go in:

```
static/
└── css/
    └── style.css
```

Example link in `base.html`:

html

```
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

---

## 10. Admin Setup and Run

### Create Admin:
bash

```
python manage.py createsuperuser
```

---

### Make Migrations:
bash

```
python manage.py makemigrations
python manage.py migrate
```

---

### Run Server:
bash

```
python manage.py runserver
```

---

## 11. Visit These URLs to Test:

* Home: `http://127.0.0.1:8000/`
* Articles: `http://127.0.0.1:8000/articles/`
* Login: `http://127.0.0.1:8000/accounts/login/`
* Signup: `http://127.0.0.1:8000/accounts/signup/`
* Admin: `http://127.0.0.1:8000/admin/`

---

