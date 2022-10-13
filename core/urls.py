from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/accidents/', include('accidents.urls')),
    path('api/incidents/', include('incidents.urls')),
    path('api/pieces/', include('pieces.urls')),
    path('api/downtime/', include('downtime.urls')),
    path('api/operation-time/', include('OT.urls')),
    path('api/headcount/', include('headcount.urls')),
    path('api/latest-records/', include('latest_records.urls')),
    path('fake_api/', include('fake_api.urls')),
]
