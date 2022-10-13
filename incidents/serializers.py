from rest_framework import serializers


from incidents.models import IncidentDetails



class IncidentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentDetails
        fields = '__all__'



class IncidentDetailsSerializerRO(serializers.ModelSerializer):

    user = serializers.SerializerMethodField('get_user')
    unity = serializers.SerializerMethodField('get_unity')
    area = serializers.SerializerMethodField('get_area')
    line = serializers.SerializerMethodField('get_line')
    turn = serializers.SerializerMethodField('get_turn')

    class Meta:
        model = IncidentDetails
        fields = ['id', 'user', 'title', 'unity', 'area', 'line', 'turn', 'description', 'date']


    def get_user(self, IncidentDetails):
        return IncidentDetails.user.username

    def get_unity(self, IncidentDetails):
        try:
            data = {
                'id': IncidentDetails.business_unity.id,
                'business_unity': IncidentDetails.business_unity.name
            }
        except:
            data = None
        return data

    
    def get_area(self, IncidentDetails):
        try:
            data = {
                'id': IncidentDetails.area.id,
                'area': IncidentDetails.area.name
            }
        except:
            data = None
        return data

    
    def get_line(self, IncidentDetails):
        try:
            data = {
                'id': IncidentDetails.line_number.id,
                'line': IncidentDetails.line_number.name
            }
        except:
            data = None
        return data


    def get_turn(self, IncidentDetails):
        try:
            data = {
                'id': IncidentDetails.turn.id,
                'start': IncidentDetails.turn.start,
                'end': IncidentDetails.turn.end
            }
        except:
            data = None
        return data    