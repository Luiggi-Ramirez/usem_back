from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.admin.models import LogEntry


from accidents.models import Accidents
from downtime.models import DowntimeDetails
from headcount.models import PeopleOnTurn
from incidents.models import IncidentDetails
from OT.models import OperationTimeDetails
from pieces.models import Production


from accidents.serializers import AccidentsSerializer
from downtime.serializers import DowntimeDetailsSerializerRO
from headcount.serializers import PeopleOnTurnSerializerRO
from incidents.serializers import IncidentDetailsSerializerRO
from OT.serializers import OperationTimeDetailsSerializerRO
from pieces.serializers import ProductionSerializerRO





class LatestRecords(APIView):
    '''view to list the data of all the endpoints that save data, in order of creation'''
    def get(self, request):

        logs = LogEntry.objects.order_by('-action_time')[:5]
        latest_records=[]
        for log in logs:
            if log.action_flag == 1:
                
                model = log.content_type.model
                
                if model == 'accidents':
                    query = Accidents.objects.filter(id = log.object_id)
                    serializer = AccidentsSerializer(query, many=True)
                    serializer.data[0]["type"] = "accident report"

                if model == 'downtimedetails':
                    query = DowntimeDetails.objects.filter(id = log.object_id)
                    serializer = DowntimeDetailsSerializerRO(query, many=True)
                    serializer.data[0]["type"] = "Down time report"

                if model == 'peopleonturn':
                    query = PeopleOnTurn.objects.filter(id = log.object_id)
                    serializer = PeopleOnTurnSerializerRO(query, many=True)
                    serializer.data[0]["type"] = "Headcount report"
                    
                if model == 'incidentdetails':
                    query = IncidentDetails.objects.filter(id = log.object_id)
                    serializer = IncidentDetailsSerializerRO(query, many=True)
                    serializer.data[0]["type"] = "Incident report"

                if model == 'operationtimedetails':
                    query = OperationTimeDetails.objects.filter(id = log.object_id)
                    serializer = OperationTimeDetailsSerializerRO(query, many=True)
                    serializer.data[0]["type"] = "operation time report"

                if model == 'production':
                    query = Production.objects.filter(id = log.object_id)
                    serializer = ProductionSerializerRO(query, many=True)
                    serializer.data[0]["type"] = "production report"

                
                latest_records.append(serializer.data[0])
                
        
        return Response(latest_records, status=status.HTTP_200_OK)