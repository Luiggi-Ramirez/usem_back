from socket import socket
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from headcount.serializers import PeopleOnTurnSerializer, WorkerSerializer
from headcount.models import PeopleOnTurn



class WorkerRegisterView(APIView):
    '''View to register a worker'''
    def post(self, request):
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 



class CreateHeadcountReport(APIView):
    '''View to register headcount reports'''
    def post(self, request):
        serializer = PeopleOnTurnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 




class TotalHeadcount(APIView):
    def get(self, request):
        queryset = PeopleOnTurn.objects.all()

        line_number = self.request.query_params.get('line_number')
        turn = self.request.query_params.get('turn')
        

        if not line_number: 
            return Response({"message": "missing query param"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            queryset = queryset.filter(line_number=line_number)
        
        if turn:
            queryset = queryset.filter(turn=turn)
        
        
        # queryset = queryset.filter(worker__gender__in=gender)
        people_working = {
            "men": len(queryset.filter(worker__gender__in="1")),
            "women": len(queryset.filter(worker__gender__in="2"))
        }
        print(people_working)

        # serializer= PeopleOnTurnSerializer(queryset,many=True)
        
        return Response(people_working, status=status.HTTP_200_OK)

