from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from pieces.models import Production
from pieces.serializers import ProductionSerializer
from latest_records.utils import custom_log_entries


class CreateProductionReport(APIView):
    '''View to register production report'''
    def post(self, request):
        serializer = ProductionSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            custom_log_entries(user_id=serializer.data['user'], model_name=Production, object_id=serializer.data['id'],  obj_repr=serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 



class ProductionData(APIView):
    '''view to add the total of the "ok" pieces and the bad ones'''
    def get(self, request):
        queryset = Production.objects.all()
        
        '''Mandatory Query Params'''
        from_date = self.request.query_params.get('from_date')
        to_date = self.request.query_params.get('to_date')
        total_pieces_percent = self.request.query_params.get('total_pieces_percent')

        if not from_date or not to_date: 
            return Response({"message": "missing query param"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            queryset = queryset.filter(date__range=[from_date, to_date])

        if not queryset:
            '''No-data handler'''
            return Response({"message" : "no data"}, status=status.HTTP_404_NOT_FOUND)

        if total_pieces_percent == 'true':  
            pieces_number = queryset.values()
            
            ok_pieces = []
            bad_pieces = []
            for i in range(len(pieces_number)):
                ok = pieces_number[i]['is_ok']
                bad = pieces_number[i]['is_bad']   
                ok_pieces.append(ok)
                bad_pieces.append(bad)
                
            ok = sum(ok_pieces)
            bad = sum(bad_pieces)

            total_production = ok + bad
            ok_pieces_percent = ok * 100 / total_production
            bad_pieces_percent = bad * 100 / total_production

          
            total_pieces = {
                "ok_pieces_percent" : round(ok_pieces_percent),
                "bad_pieces_percent" : round(bad_pieces_percent)
            }
            return Response(total_pieces, status=status.HTTP_200_OK)
        else:
            serializer= ProductionSerializer(queryset,many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
    
        