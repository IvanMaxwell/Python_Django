from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import TeacherSignUpForm
from .models import TeacherProfile
from .forms import StudentSignUpForm
from .models import StudentProfile
from accounts.models import TeacherProfile


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # change this to wherever you want
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')



def teacher_signup(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            TeacherProfile.objects.create(user=user)
            login(request, user)  # Optional: log them in after signup
            return redirect('home')  # Redirect to homepage or teacher dashboard
    else:
        form = TeacherSignUpForm()
    return render(request, 'accounts/teacher_signup.html', {'form': form})




def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            StudentProfile.objects.create(user=user)
            login(request, user)  # Optional: auto login
            return redirect('home')  # Or student dashboard
    else:
        form = StudentSignUpForm()
    return render(request, 'accounts/student_signup.html', {'form': form})


