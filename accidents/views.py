from django.utils import dateparse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from accidents.models import *
from authentication.models import CustomUser

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
            
        
        
        
        
