from rest_framework import serializers
from sita.models.assign_task import AssignTask


class AssignUserSerializer(serializers.Serializer):
    """
     AssignUserSerializer is used for assigning user
     for Incidents.
    """
    userName = serializers.CharField(max_length=100, required=True)
    selectedIncidents = serializers.ListField()

    class Meta:
        model = AssignTask
        fields = (
            "userName",
            "selectedIncidents"
        )
