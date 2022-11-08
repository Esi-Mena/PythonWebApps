from django.urls import path, include
from .views import HeroCreateView, HeroDeleteView, HeroDetailView, HeroListView, HeroUpdateView, UserAddView
from django.contrib import admin

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
    

]

