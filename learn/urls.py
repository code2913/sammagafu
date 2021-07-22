from django.urls import path
from . import views
app_name = "learn"

urlpatterns = [
    path('',views.CourseListView.as_view(),name="course"),
    path('<slug>',views.CourseDetailView.as_view(),name="course-detail"),
    path('topic/<slug>',views.TopicDetailView.as_view(),name="topic-detail"),
]
