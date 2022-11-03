from rest_framework import serializers
from sita.models.cy_feeds import CyFeeds


class CyFeedsSerializer(serializers.ModelSerializer):
    """
    Model serializer for CyFeeds information
    """
    class Meta:
        """Serializer class for CyFeeds model"""
        model = CyFeeds
        fields = (
            'feed_id', 'feed_ref_id', 'title', 'descriptions', 'shortDescriptions',
            'vulnerabilities', 'weaknesses', 'configurations', 'potentialCOAs', 'handling',
            'relatedExploitTargets', 'relatedPackages', 'version', 'informationSource_descriptions',
            'informationSource_identity', 'informationSource_roles',
            'informationSource_contributingSources', 'informationSource_time',
            'informationSource_tools', 'informationSource_references_references',
        )
