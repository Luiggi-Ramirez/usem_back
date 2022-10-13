from rest_framework import serializers
from accidents.models import *


class TurnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turns
        fields = '__all__'
        

class BusinessUnitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUnity
        fields = '__all__'
    
    
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class LineNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineNumber
        fields = '__all__'
        
        
class AccidentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccidentType
        fields = '__all__'
        

class AccidentsSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField('get_user')
    unity = serializers.SerializerMethodField('get_unity')
    area = serializers.SerializerMethodField('get_area')
    line = serializers.SerializerMethodField('get_line')
    turn = serializers.SerializerMethodField('get_turn')
    accident = serializers.SerializerMethodField('get_type_acc')

    class Meta:
        model = Accidents
        fields = ['id', 'user', 'unity', 'area', 'line', 'turn', 'accident', 'description', 'date']

    def get_user(self, Accidents):
        return Accidents.user.username

    def get_unity(self, Accidents):
        try:
            data = {
                'id': Accidents.business_unity.id,
                'business_unity': Accidents.business_unity.name
            }
        except:
            data = None
        return data

    def get_area(self, Accidents):
        try:
            data = {
                'id': Accidents.area.id,
                'area': Accidents.area.name
            }
        except:
            data = None
        return data
    
    def get_line(self, Accidents):
        try:
            data = {
                'id': Accidents.line_number.id,
                'line': Accidents.line_number.name
            }
        except:
            data = None
        return data
    
    def get_turn(self, Accidents):
        try:
            data = {
                'id': Accidents.turn.id,
                'start': Accidents.turn.start,
                'end': Accidents.turn.end
            }
        except:
            data = None
        return data

    def get_type_acc(self, Accidents):
        try:
            data = {
                'id': Accidents.accident_type.id,
                'accident_type': Accidents.accident_type.name
            }
        except:
            data = None
        return data




