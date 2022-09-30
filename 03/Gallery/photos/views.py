from django.views.generic import TemplatesView

class PhotoView(TemplatesView):
    template_name = 'photo.html'

def get_context_data(self, **kwargs):
    name = kwargs['name']

    image = f'/static/images/{name}'
    
    return {'photo': image} 


class PhotoListView(TemplatesView):
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
         photos = Path('static/images').iterdir()
         photos = [ f for i, f in (photos)]
         return dict(photos=photos())
