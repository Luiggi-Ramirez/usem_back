from rest_framework import serializers

from pieces.models import Production


class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        fields = '__all__'