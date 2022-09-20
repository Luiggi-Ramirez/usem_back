from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta

from .models import DowntimeDetails
from .serializers import DowntimeDetailsSerializer


class CreateDownTimeReport(APIView):
    '''View to register down time reports'''
    def post(self, request):
        serializer = DowntimeDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class DownTimeView(APIView):
    '''View to list line down time in minutes'''
    def get(self, request):
        queryset = DowntimeDetails.objects.all()

        line_number = self.request.query_params.get('line_number')

        '''line_number is a mandatory query param'''
        if not line_number: 
            return Response({"message": "missing query param"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            queryset = queryset.filter(line_number=line_number)

        qset_dict = queryset.values()


        start_time = []
        end_time = []
        for i in range(len(qset_dict)):
            '''Access to the attributes "start"-"end" from all the objects in the query results'''
            start = qset_dict[i]['start']
            end = qset_dict[i]['end']
            start_time.append(start.strftime("%X").split(":"))
            end_time.append(end.strftime("%X").split(":"))

          
        serializer= DowntimeDetailsSerializer(queryset,many=True)
        serialized_data = serializer.data

        for i in range(len(start_time)) and range(len(end_time)):
            
            result = timedelta(hours=int(end_time[i][0]), minutes=int(end_time[i][1])) - timedelta(hours=int(start_time[i][0]), minutes=int(start_time[i][1]))
            serialized_data[i]['downtime'] = result / 60
            

        return Response(serialized_data, status=status.HTTP_200_OK)


