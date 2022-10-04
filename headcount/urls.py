from django.urls import path
from .views import *



urlpatterns = [
    path('worker-register/', WorkerRegisterView.as_view()), 
    path('new-report/', CreateHeadcountReport.as_view()),
    path('total-headcount/', TotalHeadcount.as_view()),
]