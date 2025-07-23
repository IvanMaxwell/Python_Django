from django.shortcuts import render,redirect
from .models import Course
# Create your views here.
from django.shortcuts import render
from .forms import CourseForm
from django.contrib.auth.decorators import login_required

def course_list(request):
    # This is just sample data for now. Later we’ll use a database (models).
    courses = [
        {'title': 'Python Basics', 'description': 'Learn Python from scratch'},
        {'title': 'Web Development', 'description': 'Build websites with Django'},
    ]
    return render(request, 'course_list.html', {'courses': courses})





def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})




def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})





from django.contrib.auth.decorators import login_required
from accounts.decorator import teacher_required

@login_required
@teacher_required
def create_course(request):
    # Only teachers can get here
    return render(request, 'courses/create.html')
