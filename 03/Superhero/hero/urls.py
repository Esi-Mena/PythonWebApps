from django.views.generic import RedirectView
from django.urls import path

from hero.views import HeroDetailView, HeroListView


urlpatterns = [

    # Home
    path('', RedirectView.as_view(url='hero/')),

    # Photos
    path('hero/', HeroListView.as_view()),
    path('hero/<int:id>', HeroDetailView.as_view()),
]