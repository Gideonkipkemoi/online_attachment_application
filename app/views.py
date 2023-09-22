from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView
)


class PostListView(ListView):
    template_name = "home.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-start_date"]
    

class PostCreateView(CreateView):
    model = Post
    fields = ['position', 'company', 'description', 'start_date']
    template_name = 'post_attachment.html'
