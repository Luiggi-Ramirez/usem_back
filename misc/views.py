# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import GetAreasSerializers,LineNumberAreaSerializer
from accidents.models import Area,LineNumber

from django.shortcuts import get_object_or_404

class GetAllAreas(APIView):
    def get(self, request):
        queryset= Area.objects.all()
        serializer= GetAreasSerializers(queryset, many=True)
        serialized_data= serializer.data
        return Response(serialized_data, status.HTTP_200_OK)


class AreaLineView(APIView):
    def get(self, request, pk):
        
        area = get_object_or_404(Area, pk=pk)
        lines = LineNumber.objects.filter(area=area).order_by('name')
        area_data = GetAreasSerializers(area).data
        area_data['lines'] = LineNumberAreaSerializer(lines, many=True).data

        return Response(area_data, status=status.HTTP_200_OK)




