from accidents.models import *
from rest_framework.views import APIView
from rest_framework import status,generics
from rest_framework.response import Response
from .serializers import AreaByBUSerializer, BusinessUnitySerializer
# Create your views here.


class ListBusinessUnity(generics.ListAPIView):
    
    serializer_class = BusinessUnitySerializer
    def get_queryset(self):
        return BusinessUnity.objects.all()
    

class ListAreaByUB(generics.ListAPIView):
    
    serializer_class = AreaByBUSerializer
    def get_queryset(self):
        business_unity = self.request.query_params.get('business_unity')
        return Area.objects.filter(business_unity__name=business_unity)