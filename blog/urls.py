from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogsView.as_view(), name='all_blogs'),
    path('<int:blog_id>/', views.DetailView.as_view(), name='detail'),
]