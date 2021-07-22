from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Homepage(TemplateView):
    template_name = "index.html"

class Contact(TemplateView):
    template_name = "contact.html"

class LearnListView(TemplateView):
    template_name = "learn.html"

class AboutUs(TemplateView):
    template_name = "about.html"

class Services(TemplateView):
    template_name = "services.html"