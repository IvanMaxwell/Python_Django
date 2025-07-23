from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

# Renders the homepage template
class HomePageView(TemplateView):
    template_name = 'home.html'

# Renders the about page template
class AboutPageView(TemplateView):
    template_name = 'about.html'