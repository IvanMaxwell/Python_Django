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
    
    
