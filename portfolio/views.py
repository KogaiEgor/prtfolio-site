from django.shortcuts import render
from .models import Project
from .serializer import ProjectsSerializer
from rest_framework import views
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProjectsView(views.APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProjectsSerializer

    def get(self, request, *args, **kwargs):
        queryset = Project.objects.all()
        return render(request, 'portfolio/home.html', {'projects': queryset})


