from django.urls import path

from .views import *

urlpatterns = [
    path('get-areas/', GetAllAreas.as_view()), 
    path('get-lines/<int:pk>', AreaLineView.as_view()), 
    path('list-business-unitys', ListBusinessUnity.as_view()),
    path('list-area-byBU/',ListAreaByUB.as_view()),
]
