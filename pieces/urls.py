from django.urls import path
from .views import *


urlpatterns = [
    path('create-production-report/', CreateProductionReport.as_view()), # Create new production report
    path('production-kpi/', ProductionData.as_view()), # list the total number of pieces (ok and bad)
]