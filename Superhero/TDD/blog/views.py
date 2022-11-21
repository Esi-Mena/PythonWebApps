from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    RedirectView
)

from .models import Article,Author

class ArticleView(RedirectView):
    url = reverse_lazy('article_list')
class ArticleListView(ListView):
    template_name = 'article/list.html'
    model = Article


class ArticleDetailView(DetailView):
    template_name = 'article/detail.html'
    model = Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article/add.html"
    model = Article
    fields = '__all__'

    

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "article/edit.html"
    model = Article
    fields = '__all__'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article/delete.html'
    success_url = reverse_lazy('article_list')

def list_articles(author):
    return dict(articles=Article.objects.filter(author=author))


def get_author(user):
    return Author.objects.get_or_create(user=user)[0]


class AuthorHomeView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return '/article/'
        return f'/author/{get_author(self.request.user).pk}'


class AuthorListView(ListView):
    template_name = 'author/list.html'
    model = Author

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        return kwargs


class AuthorDetailView(DetailView):
    template_name = 'author/detail.html'
    model = Author

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs.update(list_articles(kwargs.get('object')))
        return kwargs


class AuthorAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/account_add.html'


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "registration/account/edit.html"
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
    success_url = reverse_lazy('author_home')


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "author/edit.html"
    model = Author
    fields = '__all__'


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'author/delete.html'
    success_url = reverse_lazy('author_list')

