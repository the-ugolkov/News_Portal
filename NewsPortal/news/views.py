from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2


class NewDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

# Create your views here.
