from django.urls import path
from .views import *

urlpatterns = [
    path('create-incident-report/', CreateIncidentReport.as_view()), #New incident report
    path('get-incidents-kpi/', Incident.as_view()), #incidents kpi
]