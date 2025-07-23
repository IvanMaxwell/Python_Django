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

