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
    class Meta:
        model = Accidents
        fields = '__all__'