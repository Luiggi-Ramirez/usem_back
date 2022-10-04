from rest_framework import serializers


from .models import PeopleOnTurn, Worker


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = ['name', 'last_name', 'gender' ]



class PeopleOnTurnSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeopleOnTurn
        fields = ['user', 'worker', 'business_unity', 'area', 'line_number', 'turn', 'date']