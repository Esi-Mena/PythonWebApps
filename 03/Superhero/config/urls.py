from django.urls import path
from django.urls.conf import include
from hero.views import HeroListView, HeroView

urlpatterns = [
    path('', include('hero.urls')),
    path('<str:name>', HeroView.as_view()),
    path('', HeroListView.as_view()),
]
