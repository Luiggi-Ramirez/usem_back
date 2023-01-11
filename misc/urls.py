from django.urls import path
from .views import *

urlpatterns = [
    path('list-business-unitys', ListBusinessUnity.as_view()),
    path('list-area-byBU/',ListAreaByUB.as_view()),
]
