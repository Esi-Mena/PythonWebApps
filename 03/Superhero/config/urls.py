
from django.urls import path
from django.urls.conf import include
from hero.views import HulkView, IronManView,BlackWidow,DannyDavito

urlpatterns = [
    path('', include('hero.urls')),
    path('<str:name>', HulkView.as_view()),
    path('', IronManView.as_view()),
    path('', BlackWidow.as_view()),
    path('', DannyDavito.as_view()),
    
]
