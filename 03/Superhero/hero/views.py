from pathlib import Path
from django.views.generic import TemplateView


def heroes_list():
    def heroes_details(i, f):
        caption = f'Caption for Heroes {i}' if i == 1 else None
        return dict(id=i, file=f, caption=caption)

    hero = Path('static/images').iterdir()
    hero = [heroes_details(i, f) for i, f in enumerate(hero)]
    return hero


class HeroListView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return dict(hero=heroes_list())


class HeroDetailView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        hero = heroes_list()
        p = hero[i]
        return dict(heroes=p)
