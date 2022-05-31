from django.urls import path
from .views import HomeView, PostDetailView, CreatePostView, UpdatePostView, DeletePostView
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_details'),
]
