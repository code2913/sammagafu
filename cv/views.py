from django.shortcuts import render
from django.views.generic import TemplateView
from projects.models import Project
# Create your views here.

class Homepage(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Homepage, self).get_context_data(*args, **kwargs)
        context['project'] =  Project.objects.all()
        return context

class Contact(TemplateView):
    template_name = "contact.html"

class LearnListView(TemplateView):
    template_name = "learn.html"

class AboutUs(TemplateView):
    template_name = "about.html"

class Services(TemplateView):
    template_name = "services.html"