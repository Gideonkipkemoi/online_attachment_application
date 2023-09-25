from django.shortcuts import render
from .models import Post, Apply
from django.db.models import F
from .form import StartDateForm, ApplyStartDateForm
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
    queryset = Post.objects.filter(start_date__gte=F('apply_before'))
    

class PostCreateView(CreateView):
    model = Post
    #fields = ['position', 'company', 'description']
    template_name = 'post_attachment.html'
    form_class = StartDateForm
    
class ApplyCreateView(CreateView):
    model = Apply
    '''fields = ['name', 'learning_institution',
              'applied_position',
              'curriculum_vite',
              'recommendation'
]'''
    template_name = 'apply_attachment.html'
    form_class = ApplyStartDateForm
    
