from rest_framework import serializers
from sita.models.assets import Assets


class AssetSerializer(serializers.ModelSerializer):
    """
    Model serializer for Asset information
    """
    category_name = serializers.CharField(source='category.category')
    process = serializers.CharField(source='process_id.process')

    class Meta:
        model = Assets
        fields = (
            "AssetName",
            "category_name",
            "criticality",
            "process",
        )
