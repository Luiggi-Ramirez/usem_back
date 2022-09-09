from rest_framework import serializers
from accidents.models import Accidents

class AccidentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accidents
        fields = '__all__'