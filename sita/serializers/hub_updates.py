from rest_framework import serializers
from sita.models.insights_update import HubUpdate


class AssignTaskSerializer(serializers.ModelSerializer):
    """
    Model serializer for Asset information
    """
    class Meta:
        model = HubUpdate
        fields = (
            "soar_id",
            "updates",
            "updated_by"
        )
