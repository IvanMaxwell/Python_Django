from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm


def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'home.html', {'posts': posts})



def post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)  # Bind data to form
        if form.is_valid():
            form.save()  # Save post to DB
            return redirect('home')  # Redirect to homepage
    else:
        form = BlogPostForm()  # Show empty form
    return render(request, 'post_form.html', {'form': form, 'action': 'Create'})




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




def post_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()  # Delete post
        return redirect('home')
    return render(request, 'post_confirm_delete.html', {'post': post})
