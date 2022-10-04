from rest_framework import serializers
from sita.models.functions import Function


class FunctionSerializer(serializers.ModelSerializer):
    """
    Model serializer for function information
    """
    location_name = serializers.CharField(source='location_id.location')

    class Meta:
        model = Function
        fields = (
            "function_name",
            "location_name",
        )
