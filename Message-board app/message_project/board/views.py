from django.shortcuts import render, redirect
from .models import Message
from django.utils import timezone

def home(request):
   messages = Message.objects.order_by('-timestamp')                  # Show latest first
   return render(request, 'board/home.html', {'messages': messages})

def post_message(request):
    if request.method == 'POST':
        name = request.POST['name']
        content = request.POST['content']
        Message.objects.create(name=name, content=content, timestamp=timezone.now())
        return redirect('home')
    return render(request, 'board/post_message.html')