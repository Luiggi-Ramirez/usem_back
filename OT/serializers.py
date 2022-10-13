from rest_framework import serializers

from .models import OperationTimeDetails

class OperationTimeDetailsSerializer(serializers.ModelSerializer):
    line_name = serializers.SerializerMethodField('get_line_name') #pasar al serializer de RO
    
    class Meta:
        model = OperationTimeDetails
        fields = ['id', 'user', 'line_number', 'start', 'end', 'date', 'line_name']
        

    def get_line_name(self, OperationTimeDetails):
        return OperationTimeDetails.line_number.name



class OperationTimeDetailsSerializerRO(serializers.ModelSerializer):

    user = serializers.SerializerMethodField('get_user')
    line = serializers.SerializerMethodField('get_line')
    
    class Meta:
        model = OperationTimeDetails
        fields = ['id', 'user', 'line', 'start', 'end', 'date']
        

    def get_user(self, OperationTimeDetails):
        return OperationTimeDetails.user.username

    def get_line(self, OperationTimeDetails):
        try:
            data = {
                'id': OperationTimeDetails.line_number.id,
                'line': OperationTimeDetails.line_number.name
            }
        except:
            data = None
        return data