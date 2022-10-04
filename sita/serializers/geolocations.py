from rest_framework import serializers
from sita.models.geolocations import GeoLocation


class GeoLocationSerializer(serializers.ModelSerializer):
    """
    Model serializer for Location information
    """
    entity_name = serializers.CharField(source='entity_id.entityname')

    class Meta:
        model = GeoLocation
        fields = (
            "location",
            "entity_name",
        )
