from rest_framework import serializers
from sita.models.fact_oei import FACT_OEI


class ITSMSerializer(serializers.ModelSerializer):
    """
    Model serializer for ITSM information
    """

    class Meta:
        model = FACT_OEI
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """
    Model serializer for ITSM information
    """

    selectedIncidents = serializers.CharField(max_length=100, required=True)
    Comment = serializers.CharField(max_length=100, allow_null=True)

    class Meta:
        model = FACT_OEI
        fields = (
            "SIEM_id",
            "comment")
