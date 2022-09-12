from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


from incidents.models import IncidentDetails
from incidents.serializers import IncidentDetailsSerializer



class CreateIncidentReport(APIView):
    '''View to register incident reports'''
    def post(self, request):
        serializer = IncidentDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 



class Incident(generics.ListAPIView):
    '''view to list incidents according to their query parameters'''
    serializer_class = IncidentDetailsSerializer
   
    def get_queryset(self):
        queryset = IncidentDetails.objects.all()

        count = self.request.GET.get('count')
        date = self.request.query_params.get('date')
        turn = self.request.query_params.get('turn')
        business_unity = self.request.query_params.get('business_unity')
        line_number = self.request.query_params.get('line_number')
        area = self.request.query_params.get('area')

        if date:
            queryset = queryset.filter(date=date)
        if turn:
            queryset = queryset.filter(turn=turn)
        if business_unity:
            queryset = queryset.filter(business_unity=business_unity)
        if line_number:
            queryset = queryset.filter(line_number=line_number)
        if area: 
            queryset = queryset.filter(area=area)

        return queryset

        