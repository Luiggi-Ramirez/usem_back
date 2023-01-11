from rest_framework import serializers
from accidents.models import *

class GetAreasSerializers(serializers.ModelSerializer):
    area_name = serializers.CharField(source='name')
    
    class Meta:
        model = Area
        fields = ('id', 'area_name')

class LineNumberAreaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LineNumber
        fields = '__all__'


class BusinessUnitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUnity
        fields = '__all__'

class AreaByBUSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'
