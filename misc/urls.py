from django.urls import path

from .views import GetAllAreas,AreaLineView


urlpatterns = [
    path('get-areas/', GetAllAreas.as_view()), 
    path('get-lines/<int:pk>', AreaLineView.as_view()), 
     
]