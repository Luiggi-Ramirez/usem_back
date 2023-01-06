from rest_framework import serializers
from accidents.models import *



class BusinessUnitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUnity
        fields = '__all__'
    

class AreaByBUSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'