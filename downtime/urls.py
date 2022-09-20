from django.urls import path
from .views import *

urlpatterns = [
    path('create-down-time-report/', CreateDownTimeReport.as_view()), #Create new down time report
    path('lines/', DownTimeView.as_view()), #list line down time in minute
]