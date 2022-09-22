from django.urls import path
from .views import *

urlpatterns = [
    path('create-report/', CreateOperationTimeReport.as_view()), #Create new line operation time report
    path('lines/', OperationTimeView.as_view()), #list line operation time in hours
]