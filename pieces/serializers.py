from rest_framework import serializers

from pieces.models import Production


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = '__all__'

class ProductionSerializerRO(serializers.ModelSerializer):

    user = serializers.SerializerMethodField('get_user')
    unity = serializers.SerializerMethodField('get_unity')
    area = serializers.SerializerMethodField('get_area')
    line = serializers.SerializerMethodField('get_line')
    turn = serializers.SerializerMethodField('get_turn')

    class Meta:
        model = Production
        fields = ['id', 'user', 'unity', 'area', 'line', 'turn', 'is_ok', 'is_bad', 'date']


    def get_user(self, Production):
        return Production.user.username
    
    def get_unity(self, Production):
        try:
            data = {
                'id': Production.business_unity.id,
                'business_unity': Production.business_unity.name
            }
        except:
            data = None
        return data

    
    def get_area(self, Production):
        try:
            data = {
                'id': Production.area.id,
                'area': Production.area.name
            }
        except:
            data = None
        return data

    
    def get_line(self, Production):
        try:
            data = {
                'id': Production.line_number.id,
                'line': Production.line_number.name
            }
        except:
            data = None
        return data


    def get_turn(self, Production):
        try:
            data = {
                'id': Production.turn.id,
                'start': Production.turn.start,
                'end': Production.turn.end
            }
        except:
            data = None
        return data    