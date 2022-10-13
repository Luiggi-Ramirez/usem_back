from rest_framework import serializers


from .models import PeopleOnTurn, Worker


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = ['name', 'last_name', 'gender' ]



class PeopleOnTurnSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeopleOnTurn
        fields = ['id', 'user', 'worker', 'business_unity', 'area', 'line_number', 'turn', 'date']



class PeopleOnTurnSerializerRO(serializers.ModelSerializer):

    worker = serializers.SerializerMethodField('get_worker')
    unity = serializers.SerializerMethodField('get_unity')
    area = serializers.SerializerMethodField('get_area')
    line = serializers.SerializerMethodField('get_line')
    turn = serializers.SerializerMethodField('get_turn')

    class Meta:
        model = PeopleOnTurn
        fields = ['id', 'worker', 'unity', 'area', 'line', 'turn', 'date']

    def get_worker(self, PeopleOnTurn):
        try:
            data = {
                'id': PeopleOnTurn.worker.id,
                'name': PeopleOnTurn.worker.name,
                'last_name': PeopleOnTurn.worker.last_name,
            }
        except:
            data = None
        return data
    
    def get_unity(self, PeopleOnTurn):
        try:
            data = {
                'id': PeopleOnTurn.business_unity.id,
                'business_unity': PeopleOnTurn.business_unity.name
            }
        except:
            data = None
        return data

    
    def get_area(self, PeopleOnTurn):
        try:
            data = {
                'id': PeopleOnTurn.area.id,
                'area': PeopleOnTurn.area.name
            }
        except:
            data = None
        return data

    
    def get_line(self, PeopleOnTurn):
        try:
            data = {
                'id': PeopleOnTurn.line_number.id,
                'line': PeopleOnTurn.line_number.name
            }
        except:
            data = None
        return data


    def get_turn(self, PeopleOnTurn):
        try:
            data = {
                'id': PeopleOnTurn.turn.id,
                'start': PeopleOnTurn.turn.start,
                'end': PeopleOnTurn.turn.end
            }
        except:
            data = None
        return data    