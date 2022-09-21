from django.views.generic import TemplatesView

class PhotoView(TemplatesView):
    template_name = 'photo.html'

def get_context_data(self, **kwargs):
    
    return {'photo': "/static/images/chapter-2.jpg"}

"/static/images/chapter-1.jpg"