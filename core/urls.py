from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/accidents/', include('accidents.urls')),
    path('api/incidents/', include('incidents.urls')),
    path('api/pieces/', include('pieces.urls')),
]
