from rest_framework import serializers


class CredentialSerializer(serializers.Serializer):
    """
     Serializer class for credential serializer json field.
    """

    filename = serializers.CharField(max_length=100)
    path = serializers.CharField(max_length=100)
