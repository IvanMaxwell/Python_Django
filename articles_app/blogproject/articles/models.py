from django.db import models

# Create your models here.
# articles/models.py

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)  # Article title
    content = models.TextField()              # Main content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp on creation

    def __str__(self):
        return self.title  # Used in admin panel and shell

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')  # Link to article
    author = models.CharField(max_length=100)  # Name of commenter
    text = models.TextField()                  # Comment body
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author}'
