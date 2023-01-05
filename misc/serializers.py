from rest_framework import serializers
from accidents.models import *


class AreaByBUSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'