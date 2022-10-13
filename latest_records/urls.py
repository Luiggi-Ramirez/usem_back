from django.urls import path

from latest_records.views import LatestRecords

urlpatterns = [
    path('list/', LatestRecords.as_view()), 
     
]