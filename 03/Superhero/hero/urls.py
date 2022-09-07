from django.urls import path
from .views import BlackWidow, HulkView, IndexView, IronManView, DannyDavito

urlpatterns = [
    path('', IndexView.as_view()),
    path('hulk', HulkView.as_view()),
    path('ironman', IronManView.as_view()),
    path('blackwidow', BlackWidow.as_view()),
    path('DannyDavito',DannyDavito.as_view()),
    
]
