from .views import ProjectsView
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', ProjectsView.as_view(), name="home"),
]

urlpatterns = format_suffix_patterns(urlpatterns)