from rest_framework import serializers
from accidents.models import *

class GetAreasSerializers(serializers.ModelSerializer):
    area_name = serializers.CharField(source='name')
    
    class Meta:
        model = Area
        fields = ('id', 'area_name')

class LineNumberAreaSerializer(serializers.ModelSerializer):
    line_name = serializers.CharField(source='name')
    
    class Meta:
        model = LineNumber
        fields = ('line_name',)

