from rest_framework import serializers

from .models import DowntimeDetails

class DowntimeDetailsSerializer(serializers.ModelSerializer):
    line_name = serializers.SerializerMethodField('get_line_name')
    
    class Meta:
        model = DowntimeDetails
        fields = ['id', 'user', 'line_number', 'start', 'end', 'date', 'line_name']
        

    def get_line_name(self, DowntimeDetails):
        return DowntimeDetails.line_number.name



class DowntimeDetailsSerializerRO(serializers.ModelSerializer):

    line = serializers.SerializerMethodField('get_line')    

    class Meta:
        model = DowntimeDetails
        fields = ['id', 'line', 'start', 'end', 'date']

    
    def get_line(self, DowntimeDetails):
        try:
            data = {
                'id': DowntimeDetails.line_number.id,
                'line': DowntimeDetails.line_number.name
            }
        except:
            data = None
        return data
        