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
