from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Blog

class CreateBlogView(CreateView):
    model = Blog
    fields = ['title', 'image', 'category', 'summary', 'content', 'draft']
    template_name = 'blog/create_blog.html'
    success_url = reverse_lazy('blog_list')  

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)

class MyBlogsView(ListView):
    model = Blog
    template_name = 'blog/my_blogs.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(draft=False).order_by('-created_at')


from django.views.generic import DetailView
from .models import Blog

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'
