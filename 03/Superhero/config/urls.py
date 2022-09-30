from django.views.generic import RedirectView
from django.urls import path

from hero.views import HeroDetailView, HeroListView


urlpatterns = [

    # Home
    path('', RedirectView.as_view(url='heroes/')),

    # Photos
    path('heroes/', HeroListView.as_view()),
    path('heroes/<int:id>', HeroDetailView.as_view()),
]