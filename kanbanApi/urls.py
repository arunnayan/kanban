from django.urls import path

from .views import ProjectView

app_name = "projects"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('projects/', ProjectView.as_view()),
]
