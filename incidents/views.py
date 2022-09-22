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



class Incident(APIView):
    '''view to list incidents according to their query parameters'''
    
    def get(self, request, *args, **kwargs):
        queryset = IncidentDetails.objects.all()

        count = self.request.GET.get('count')
        from_date = self.request.query_params.get('from_date')
        to_date = self.request.query_params.get('to_date')
        turn = self.request.query_params.get('turn')
        business_unity = self.request.query_params.get('business_unity')
        line_number = self.request.query_params.get('line_number')
        area = self.request.query_params.get('area')

        

        if from_date or to_date:
            queryset = queryset.filter(date__range=[from_date, to_date])
        if turn:
            queryset = queryset.filter(turn=turn)
        if business_unity:
            queryset = queryset.filter(business_unity=business_unity)
        if line_number:
            queryset = queryset.filter(line_number=line_number)
        if area: 
            queryset = queryset.filter(area=area)
        if count == "true": 
            reported_incidents = {
                "reported_incidents" : len(queryset) }
            return Response(reported_incidents, status=status.HTTP_200_OK)

        '''No-data handler'''
        if not queryset:
            return Response({"message" : "no data"}, status=status.HTTP_404_NOT_FOUND)
        else:
        
        
            serializer= IncidentDetailsSerializer(queryset,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        

        