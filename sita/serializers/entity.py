from rest_framework import serializers
from sita.models.entity import Entity


class EntitySerializer(serializers.ModelSerializer):
    """
    Model serializer for Entity information
    """

    class Meta:
        model = Entity
        fields = (
            "entityname",
        )
