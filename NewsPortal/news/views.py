from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post
from .filters import PostFilter


class NewsList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10


class SearchList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news_search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
# Create your views here.
