from django.shortcuts import render

# Create your views here.
# articles/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm, CommentForm

# List all articles
def article_list(request):
    articles = Article.objects.all().order_by('-created_at')  # Newest first
    return render(request, 'articles/article_list.html', {'articles': articles})

# Show one article + comments
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article  # Link comment to the current article
            comment.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = CommentForm()
    
    return render(request, 'articles/article_detail.html', {
        'article': article,
        'comments': comments,
        'form': form
    })

# Create a new article
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'articles/article_form.html', {'form': form})

# Edit an existing article
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/article_form.html', {'form': form})

# Delete article
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')
