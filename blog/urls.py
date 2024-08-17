from django.urls import path
from .views import BlogListView, BlogDetailView, CreateBlogView, MyBlogsView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('create/', CreateBlogView.as_view(), name='create_blog'),
    path('my/', MyBlogsView.as_view(), name='my_blogs'),
]