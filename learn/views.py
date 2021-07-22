from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Course,Topic,CourseCategory
# Create your views here.


class CourseListView(ListView):
    model = Course
    context_object_name = "course"
    template_name = "learn.html"

    def get_context_data(self,**kwargs):
        context = super(CourseListView,self).get_context_data(**kwargs)
        context['category'] = CourseCategory.objects.all()
        return context

class CourseDetailView(DetailView):
    model = Course
    context_object_name = "course"
    template_name = "learn-detail.html"

class TopicDetailView(DetailView):
    model = Topic
    context_object_name = "topic"
    template_name = "topic-detail.html"