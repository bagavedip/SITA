from rest_framework import serializers
from sita.models.perspective import Perspective


class PerspectiveSerializer(serializers.ModelSerializer):
    """
    Model serializer for Process information
    """

    class Meta:
        model = Perspective
        fields = (
            "perspective_type",
            "action_type",
            "status_type",
            "criticality_type",
            "incident_id",
            "perspective_title",
            "perspective",
            "recommendation",
            # "tags",
            "donut_left_graph",
            "donut_right_graph",
            "comparative_left_graph",
            "comparative_right_graph",
            "incident_start_date_time",
            "incident_end_date_time",
        )


class PerspectiveUpdateSerializer(serializers.ModelSerializer):
    """
     Model serializer for Process information
     """
    class Meta:
        model = Perspective
        fields = (
            "perspective_type",
            "action_type",
            "status_type",
            "criticality_type",
            "incident_id",
            "perspective_title",
            "perspective",
            "recommendation",
            "tags",
            "donut_left_graph",
            "donut_right_graph",
            "comparative_left_graph",
            "comparative_right_graph",
            "incident_start_date_time",
            "incident_end_date_time",
        )

