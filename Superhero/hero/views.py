from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Superhero, Article
from django.contrib.auth.forms import UserCreationForm

class HeroListView(ListView):
    template_name = 'hero/list.html'
    model = Superhero


class HeroDetailView(DetailView):
    template_name = 'hero/detail.html'
    model = Superhero


class HeroCreateView(LoginRequiredMixin,CreateView):
    template_name = "hero/add.html"
    model = Superhero
    fields = '__all__'


class HeroUpdateView(LoginRequiredMixin,UpdateView):
    template_name = "hero/edit.html"
    model = Superhero
    fields = '__all__'


class HeroDeleteView(LoginRequiredMixin,DeleteView):
    model = Superhero
    template_name = 'hero/delete.html'
    success_url = reverse_lazy('hero_list')

class UserAddView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/add.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article_add.html"
    model = Article
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "article_edit.html"
    model = Article
    fields = '__all__'

