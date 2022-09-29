from django.urls import path
from .views import *

urlpatterns = [
    path('list-incidents-test/', Incident.as_view()), 
    path('list-accidents-test/', FirstFive.as_view()), 
    path('list-downtime-test/', Downtime.as_view()), 
    path('list-production-test/', Pieces.as_view()), 
    path('list-first-five/', FirstFive.as_view()), 
    
]