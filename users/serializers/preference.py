from rest_framework import serializers
from users.models.preference import Preference


class PreferenceSerializer(serializers.ModelSerializer):
    """
    Serializer for preference model
    """
    class Meta:
        model = Preference
        fields = (
            'user',
            'session',
        )
