from accidents.models import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import AreaByBUSerializer
# Create your views here.


class ListAreaByUB(APIView):
    def post(self, request):
        business_unity_id = int(request.data['business_unity_id'])
        areas = Area.objects.filter(business_unity=business_unity_id)
        return Response(AreaByBUSerializer(areas,many=True).data, status = status.HTTP_200_OK)
