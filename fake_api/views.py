from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Incident(APIView):

    def get(self, request):
            
        incidents_list = [
        {
            "id": 1,
            "title": "fallo en motor",
            "description": "El abánico huele a pelo quemado",
            "date": "2022-09-13",
            "user": 1,
            "business_unity": 5,
            "area": 1,
            "line_number": 1,
            "turn": 3
        },
        {
            "id": 2,
            "title": "Computadora lenta",
            "description": "pónganle SSD",
            "date": "2022-09-15",
            "user": 1,
            "business_unity": 6,
            "area": 2,
            "line_number": 2,
            "turn": 1
        },
        {
            "id": 3,
            "title": "Se acabaron las sabritas",
            "description": "Hasta los cheetos de bolita, caminaron",
            "date": "2022-09-17",
            "user": 1,
            "business_unity": 7,
            "area": 3,
            "line_number": 3,
            "turn": 2
        },
        {
            "id": 4,
            "title": "Lámparas dañadas",
            "description": "No encienden correctamente",
            "date": "2022-09-20",
            "user": 1,
            "business_unity": 7,
            "area": 3,
            "line_number": 3,
            "turn": 3
        }
        ]

        return Response(incidents_list, status=status.HTTP_200_OK)
    

class Downtime(APIView):

    def get(self, request):

        d_time = [
        {
            "user": 1,
            "line_number": 3,
            "start": "22:00:00",
            "end": "22:45:00",
            "date": "2022-09-06",
            "line_name": "896",
            "downtime": 45
        },
        {
            "user": 1,
            "line_number": 3,
            "start": "07:00:00",
            "end": "09:45:00",
            "date": "2022-09-08",
            "line_name": "896",
            "downtime": 165
        },
        {
            "user": 1,
            "line_number": 3,
            "start": "07:00:00",
            "end": "09:45:00",
            "date": "2022-09-11",
            "line_name": "896",
            "downtime": 165
        },
        {
            "user": 1,
            "line_number": 3,
            "start": "19:00:00",
            "end": "19:23:00",
            "date": "2022-09-19",
            "line_name": "896",
            "downtime": 23
        }
        ]

        return Response(d_time, status=status.HTTP_200_OK)



class Pieces(APIView):

    def get(self, request):
        production = [
        {
            "id": 3,
            "is_ok": 600,
            "is_bad": 400,
            "date": "2022-09-03",
            "user": 1,
            "business_unity": 6,
            "area": 2,
            "line_number": 2,
            "turn": 2
        },
        {
            "id": 4,
            "is_ok": 900,
            "is_bad": 200,
            "date": "2022-09-05",
            "user": 1,
            "business_unity": 7,
            "area": 2,
            "line_number": 3,
            "turn": 2
        },
        {
            "id": 5,
            "is_ok": 400,
            "is_bad": 50,
            "date": "2022-09-07",
            "user": 1,
            "business_unity": 7,
            "area": 2,
            "line_number": 3,
            "turn": 2
        },
        {
            "id": 6,
            "is_ok": 800,
            "is_bad": 200,
            "date": "2022-09-10",
            "user": 1,
            "business_unity": 7,
            "area": 2,
            "line_number": 3,
            "turn": 2
        }
        ]

        return Response(production, status=status.HTTP_200_OK)


class FirstFive(APIView):

    def get(self, request):
        first_five = [
        {
            "id": 3,
            "is_ok": 600,
            "is_bad": 400,
            "date": "2022-09-03",
            "user": 1,
            "business_unity": 6,
            "area": 2,
            "line_number": 2,
            "turn": 2
        },
        {
            "id": 4,
            "title": "Lámparas dañadas",
            "description": "No encienden correctamente",
            "date": "2022-09-20",
            "user": 1,
            "business_unity": 7,
            "area": 3,
            "line_number": 3,
            "turn": 3
        },
        {
            "id": 5,
            "is_ok": 400,
            "is_bad": 50,
            "date": "2022-09-07",
            "user": 1,
            "business_unity": 7,
            "area": 2,
            "line_number": 3,
            "turn": 2
        },
        {
            "user": 1,
            "line_number": 3,
            "start": "19:00:00",
            "end": "19:23:00",
            "date": "2022-09-19",
            "line_name": "896",
            "downtime": 23
        },
        {
            "id": 2,
            "title": "Computadora lenta",
            "description": "pónganle SSD",
            "date": "2022-09-15",
            "user": 1,
            "business_unity": 6,
            "area": 2,
            "line_number": 2,
            "turn": 1
        }
        ]

        return Response(first_five, status=status.HTTP_200_OK)