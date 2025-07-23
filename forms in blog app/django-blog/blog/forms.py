from django import forms  # Django's forms module
from .models import BlogPost  # Import the BlogPost model

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost  # Link form to BlogPost model
        fields = ['title', 'content']  # Include these fields in the form
