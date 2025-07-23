from django.shortcuts import render
from .models import Quiz
from .forms import QuizForm
from django.contrib.auth.decorators import login_required





def quiz_list(request):
    # Temporary quiz data
    quizzes = [
        {'title': 'Python Quiz', 'questions': 5},
        {'title': 'HTML Basics', 'questions': 3},
    ]
    return render(request, 'quiz_list.html', {'quizzes': quizzes})




def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})



def add_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quiz_list')
    else:
        form = QuizForm()
    return render(request, 'add_quiz.html', {'form': form})
