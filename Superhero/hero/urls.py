from django.urls import path, include
from .views import HeroCreateView, HeroDeleteView, HeroDetailView, HeroListView, HeroUpdateView, UserAddView,ArticleListView,ArticleCreateView,ArticleDetailView,ArticleUpdateView,ArticleDeleteView
from django.contrib import admin

urlpatterns = [

    path('',                HeroListView.as_view(),    name='hero_list'),
    path('<int:pk>',        HeroDetailView.as_view(),  name='hero_detail'),
    path('add',             HeroCreateView.as_view(),  name='hero_add'),
    path('<int:pk>/',       HeroUpdateView.as_view(),  name='hero_edit'),
    path('<int:pk>/delete', HeroDeleteView.as_view(),  name='hero_delete'),
    

    path('article/',                  ArticleListView.as_view(),    name='article_list'),
    path('article/<int:pk>',          ArticleDetailView.as_view(),  name='article_detail'),
    path('article/add',               ArticleCreateView.as_view(),  name='article_add'),
    path('article/<int:pk>/',         ArticleUpdateView.as_view(),  name='article_edit'),
    path('article/<int:pk>/delete',   ArticleDeleteView.as_view(),  name='article_delete'),


    #path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('accounts/signup/',            UserAddView.as_view(),      name='signup'),
 
    
    path('admin/', admin.site.urls),

    

]

