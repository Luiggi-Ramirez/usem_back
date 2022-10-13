from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta

from latest_records.utils import custom_log_entries
from .models import DowntimeDetails
from .serializers import DowntimeDetailsSerializer


class CreateDownTimeReport(APIView):
    '''View to register down time reports'''
    def post(self, request):
        serializer = DowntimeDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            custom_log_entries(user_id=serializer.data['user'], model_name=DowntimeDetails, object_id=serializer.data['id'],  obj_repr=serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class DownTimeView(APIView):
    '''View to list line down time in minutes'''
    def get(self, request):
        queryset = DowntimeDetails.objects.all()

        line_number = self.request.query_params.get('line_number')
        from_date = self.request.query_params.get('from_date')
        to_date = self.request.query_params.get('to_date')
        total_line_dt = self. request.query_params.get('total_line_dt')

        '''line_number is a mandatory query param'''
        if not line_number: 
            return Response({"message": "missing query param"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            queryset = queryset.filter(line_number=line_number)

        '''filter by a range of dates'''
        if from_date or to_date:
            
            queryset = queryset.filter(date__range=[from_date, to_date])
        
        '''No-data handler'''
        if not queryset:
            
            return Response({"message" : "no data"}, status=status.HTTP_404_NOT_FOUND)
        else:

            qset_dict = queryset.values() #transform query in a dict

            serializer= DowntimeDetailsSerializer(queryset,many=True)
            serialized_data = serializer.data

            
            total_dt = []
            total_res = {}
            for i in range(len(qset_dict)):
                '''Access to the attributes "start"-"end" from all the objects in the query results'''
                start = qset_dict[i]['start']
                end = qset_dict[i]['end']

                # calculation to get the difference time
                result = timedelta(hours=end.hour, minutes=end.minute) - timedelta(hours=start.hour, minutes=start.minute)

                '''convert the result in minutes and save it in a new property called
                "downtime" in the serializer'''
                serialized_data[i]['downtime'] = round(result.total_seconds() / 60)

                '''convert the result in minutes and save it in the list
                 "total_dt" to add all the results and get the total down time'''
                total_dt.append(round(result.total_seconds() / 60))

                #get the name of the line to save it as a property in the json that will be sent as a response
                total_res["line"] = serialized_data[i]["line_name"]
                

            total_downtime = sum(total_dt) # sum of all the results to obtain the total down time

            # Save the total down time in the json that will be sent as a response
            total_res["total_downtime"] = total_downtime 
        
            if total_line_dt == 'true':
            
                return Response(total_res, status=status.HTTP_200_OK)
            

            return Response(serialized_data, status=status.HTTP_200_OK)

