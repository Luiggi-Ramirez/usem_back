from rest_framework import serializers


from incidents.models import IncidentDetails



class IncidentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentDetails
        fields = '__all__'