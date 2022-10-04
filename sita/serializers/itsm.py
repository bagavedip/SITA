from rest_framework import serializers
from sita.models.stg_itsm import STG_ITSM


class ITSMSerializer(serializers.ModelSerializer):
    """
    Model serializer for ITSM information
    """

    class Meta:
        model = STG_ITSM
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """
    Model serializer for ITSM information
    """

    selectedIncidents = serializers.CharField(max_length=100, required=True)
    Comment = serializers.CharField(max_length=100, allow_null=True)

    class Meta:
        model = STG_ITSM
        fields = (
            "SIEM_id",
            "comment")
