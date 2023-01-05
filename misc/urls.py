from django.urls import path
from .views import *

urlpatterns = [
    path('list-area-byBU/',ListAreaByUB.as_view()),
]
