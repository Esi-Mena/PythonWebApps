from django.urls import path, include
from .views import HeroCreateView, HeroDeleteView, HeroDetailView, HeroListView, HeroUpdateView, UserAddView,ArticleListView,ArticleCreateView,ArticleDeleteView,ArticleDetailView,ArticleUpdateView
from django.contrib import admin
from .views_author import AuthorAddView,AuthorDeleteView,AuthorDetailView,AuthorListView,AuthorUpdateView,AuthorHomeView
from django.views.generic import RedirectView

urlpatterns = [

    path('',                HeroListView.as_view(),    name='hero_list'),
    path('<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('add',             HeroCreateView.as_view(),  name='hero_add'),
    path('<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),
    


    #path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('accounts/signup/',            UserAddView.as_view(),      name='signup'),
 
    
    path('admin/', admin.site.urls),

    
    path('article/',                  ArticleListView.as_view(),    name='article_list'),
    path('article/<int:pk>',          ArticleDetailView.as_view(),  name='article_detail'),
    path('article/add',               ArticleCreateView.as_view(),  name='article_add'),
    path('article/<int:pk>/',         ArticleUpdateView.as_view(),  name='article_edit'),
    path('article/<int:pk>/delete',   ArticleDeleteView.as_view(),  name='article_delete'),

    path('',                           RedirectView.as_view(url='author/home')),
    path('author/',                    AuthorListView.as_view(),    name='author_list'),
    path('author/home',                AuthorHomeView.as_view(),    name='author_home'),
    path('author/<int:pk>',            AuthorDetailView.as_view(),  name='author_detail'),
    path('author/add/',                AuthorAddView.as_view(),     name='author_add'),
    path('author/<int:pk>/',           AuthorUpdateView.as_view(),  name='author_edit'),
    path('author/<int:pk>/delete',     AuthorDeleteView.as_view(),  name='author_delete'),

    

]

