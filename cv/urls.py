from django.urls import path
from .import views

app_name = "pages"

urlpatterns = [
    path('',views.Homepage.as_view(),name="homepage"),
    path('contact',views.Contact.as_view(),name="contact"),
    path('about',views.AboutUs.as_view(),name="about"),
    # path('learn/',views.LearnListView.as_view(),name="learn"),
    path('services/',views.Services.as_view(),name="service"),
]
