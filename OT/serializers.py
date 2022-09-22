from rest_framework import serializers

from .models import OperationTimeDetails

class OperationTimeDetailsSerializer(serializers.ModelSerializer):
    line_name = serializers.SerializerMethodField('get_line_name')
    
    class Meta:
        model = OperationTimeDetails
        fields = ['user', 'line_number', 'start', 'end', 'date', 'line_name']
        

    def get_line_name(self, OperationTimeDetails):
        return OperationTimeDetails.line_number.name