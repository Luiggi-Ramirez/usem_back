from rest_framework import serializers

from .models import DowntimeDetails

class DowntimeDetailsSerializer(serializers.ModelSerializer):
    line_name = serializers.SerializerMethodField('get_line_name')
    
    class Meta:
        model = DowntimeDetails
        fields = ['user', 'line_number', 'start', 'end', 'date', 'line_name']
        

    def get_line_name(self, DowntimeDetails):
        return DowntimeDetails.line_number.name