from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta

from .models import OperationTimeDetails
from .serializers import OperationTimeDetailsSerializer


class CreateOperationTimeReport(APIView):
    '''View to register operation time reports'''
    def post(self, request):
        serializer = OperationTimeDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 



class OperationTimeView(APIView):
    '''View to list line operation time in hours'''
    def get(self, request):
        queryset = OperationTimeDetails.objects.all()

        line_number = self.request.query_params.get('line_number')
        from_date = self.request.query_params.get('from_date')
        to_date = self.request.query_params.get('to_date')
        total_line_ot = self. request.query_params.get('total_line_ot')

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

            serializer= OperationTimeDetailsSerializer(queryset,many=True)
            serialized_data = serializer.data

            
            total_ot = []
            total_res = {}


            def save_result(result):
                '''convert the result in hours and save it in a new property called
                "operation_time" in the serializer object'''
                serialized_data[i]['operation_time'] = {
                    "hours": round(result.total_seconds() / 3600),
                    "minutes" :round(result.total_seconds() / 60 % 60)
                    }

                '''convert the result in hours and save it in the list
                "total_dt" to add all the results and get the total operation time'''
                total_ot.append(result.total_seconds() / 3600)

                #get the name of the line to save it as a property in the json that will be sent as a response
                total_res["line"] = serialized_data[i]["line_name"]


            for i in range(len(qset_dict)):
                '''Access to the attributes "start"-"end" from all the objects in the query results'''
                start = qset_dict[i]['start']
                end = qset_dict[i]['end']

                # calculation to get the difference time
                end_hour = timedelta(hours=end.hour, minutes=end.minute)
                start_hour = timedelta(hours=start.hour, minutes=start.minute)
    
                if start_hour > end_hour:
                    result = timedelta(days=1, hours=end.hour, minutes=end.minute) - timedelta(hours=start.hour, minutes=start.minute)
                    
                    save_result(result)
                else:
                    result = end_hour - start_hour
                    save_result(result)
                    
                
            
            total_operation_time = sum(total_ot) # sum of all the results to obtain the total operation time
            print(total_operation_time)
            # Save the total operation time in the json that will be sent as a response
            total_res["total_op_time"] = {
                "hours":round(total_operation_time),
                "minutes": round(total_operation_time * 60 % 60)
                
            }
        
            if total_line_ot == 'true':
            
                return Response(total_res, status=status.HTTP_200_OK)
            
        
            return Response(serialized_data, status=status.HTTP_200_OK)
