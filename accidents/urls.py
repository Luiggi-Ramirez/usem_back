from django.urls import path
from accidents.views import *

urlpatterns = [
    path('create-report/<int:user_id>/', CreatAccidentReport.as_view()),
    path('list-turns', ListTurns.as_view()),
    path('list-business-unitys', ListBusinessUnity.as_view()),
    path('list-area', ListArea.as_view()),
    path('list-line-number', ListLineNumber.as_view()),
    path('list-accident-type', ListAccidentType.as_view()),
    path('all/', ListAccidents.as_view()),
]
