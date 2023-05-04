from django.shortcuts import render, get_object_or_404
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import views
from rest_framework.permissions import AllowAny


class BlogsView(views.APIView):
    permission_classes = [AllowAny]
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        queryset = Blog.objects.order_by('-id')[0:5]
        return render(request, 'blog/all_blogs.html', {'blogs': queryset})

class DetailView(views.APIView):
    permission_classes = [AllowAny]
    serializer_class = BlogSerializer

    def get(self, request, blog_id, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=blog_id)
        return render(request, 'blog/detail.html', {'blog': blog})