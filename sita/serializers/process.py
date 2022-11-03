from rest_framework import serializers
from sita.models.process import Process


class ProcessSerializer(serializers.ModelSerializer):
    """
    Model serializer for Process information
    """
    
    function_name = serializers.CharField(source='function_id.function_name')
    
    class Meta:
        model = Process
        fields = (
            "process",
            "function_name",
        )
