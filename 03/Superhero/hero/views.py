from pathlib import Path
from django.views.generic import TemplateView


def hero_list():
    def hero_details(i, f):
        caption = f'Caption for Hero {i}' if i == 1 else None
        return dict(id=i, file=f, caption=caption)

    hero = Path('static/images').iterdir()
    hero = [hero_details(i, f) for i, f in enumerate(hero)]
    return hero


class PhotoListView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return dict(hero=hero_list())


class PhotoDetailView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        hero = hero_list()
        p = hero[i]
        return dict(hero=p)
