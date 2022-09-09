from django.urls import path
from accidents.views import CreatAccidentReport

urlpatterns = [
    path('create-report/<int:user_id>/', CreatAccidentReport.as_view()),
]