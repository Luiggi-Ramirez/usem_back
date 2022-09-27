from django.utils import dateparse

from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from accidents.models import *
from authentication.models import CustomUser
from accidents.serializers import *

class CreatAccidentReport(APIView):
    def post(self, request, user_id):
        business_unity_id = int(request.data['business_unity_id'])
        area_id = int(request.data['area_id'])
        line_number_id = int(request.data['line_number_id'])
        turn_id = int(request.data['turn_id'])
        accident_type_id = int(request.data['accident_type_id'])
        description = request.data['description']
        date = dateparse.parse_date(request.data['date'])
        
        try:
            user = CustomUser.objects.get(id = user_id)
            b_u = BusinessUnity.objects.get(id = business_unity_id)
            area = Area.objects.get(id = area_id)
            line_number = LineNumber.objects.get(id = line_number_id)
            turn = Turns.objects.get(id = turn_id)
            accident_type = AccidentType.objects.get(id = accident_type_id)
            
            Accidents.objects.create(user = user, business_unity = b_u, area = area, line_number = line_number, turn = turn, accident_type = accident_type, description = description, date= date)
            
            data = {'msg': 'Reporte de accidente creado'}
            code = status.HTTP_201_CREATED
        except Exception as error:
            print(error)
            data = {'error': 'Usuario no registrado'}
            code = status.HTTP_404_NOT_FOUND
            
        return Response(data, status = code)
            
        
class ListTurns(generics.ListAPIView):
    
    serializer_class = TurnsSerializer
    def get_queryset(self):
        return Turns.objects.all()


class ListBusinessUnity(generics.ListAPIView):
    
    serializer_class = BusinessUnitySerializer
    def get_queryset(self):
        return BusinessUnity.objects.all()
    

class ListArea(generics.ListAPIView):
    
    serializer_class = AreaSerializer
    def get_queryset(self):
        return Area.objects.all()


class ListLineNumber(generics.ListAPIView):
    
    serializer_class = LineNumberSerializer
    def get_queryset(self):
        return LineNumber.objects.all()
    

class ListAccidentType(generics.ListAPIView):
    
    serializer_class = AccidentTypeSerializer
    def get_queryset(self):
        return AccidentType.objects.all()
    

class ListAccidents(generics.ListAPIView):
    
    serializer_class = AccidentsSerializer
    def get_queryset(self):
        return Accidents.objects.all()


class ListAccidentsById(generics.ListAPIView):

    serializer_class = AccidentsSerializer
    def get_queryset(self):
        accident_id = self.request.query_params.get('accident-id')
        queryset = Accidents.objects.filter(id = accident_id)
        return queryset


class ListAccidentsByType(generics.ListAPIView):

    serializer_class = AccidentsSerializer
    def get_queryset(self):
        type_accident_id = self.request.query_params.get('type-accident-id')
        queryset = Accidents.objects.filter(accident_type__id = type_accident_id)
        return queryset


class ListAccidentsByDate(generics.ListAPIView):

    serializer_class = AccidentsSerializer
    def get_queryset(self):
        date = dateparse.parse_date(self.request.query_params.get('date'))
        queryset = Accidents.objects.filter(date = date)
        return queryset
