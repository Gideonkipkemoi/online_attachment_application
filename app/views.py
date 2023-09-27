from django.shortcuts import render
from .models import Post, Apply
from django.db.models import F
from .form import StartDateForm, ApplyStartDateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView
)
from .mixins import GroupRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

class PostListView(ListView):
    template_name = "home.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-start_date"]
    queryset = Post.objects.filter(start_date__gte=F('apply_before'))
    

class PostCreateView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin,CreateView):
    model = Post
    #fields = ['position', 'company', 'description']
    template_name = 'post_attachment.html'
    form_class = StartDateForm
    group_required = [u'supervisor']
    permission_denied_message = "you do not have access to this module "
    success_message = "%(position)s successfully created"
    
    
class ApplyCreateView(LoginRequiredMixin, GroupRequiredMixin, SuccessMessageMixin, CreateView):
    model = Apply, Post
    '''fields = ['name', 'learning_institution',
              'applied_position',
              'curriculum_vite',
              'recommendation'
]'''
    template_name = 'apply_attachment.html'
    form_class = ApplyStartDateForm
    group_required = [u'student']
    success_message = "%(applied_position)s successfully applied"
    queryset = Post.objects.filter(apply_before__gte=F('apply_before'))
    
    
