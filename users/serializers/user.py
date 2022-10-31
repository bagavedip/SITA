from rest_framework import serializers

from SITA_backend.custom_serializer import DynamicFieldSerializerMixin
from users.models import User


class UserSerializer(serializers.Serializer):
    """
     Serializer for User Models
    """
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(max_length=256, required=False)
    last_name = serializers.CharField(max_length=256, required=False)
    is_admin = serializers.BooleanField(required=True)
    role_id = serializers.IntegerField(source='role_id.id',required = False)
    role = serializers.CharField(source='role_id.name',required = False)
    phone_code = serializers.CharField(max_length=10, required=False)
    phone_number = serializers.CharField(max_length=20, required=False)
    # profile_photo = None if bool(serializers.FileField) is False else serializers.FileField.read()
    class Meta:
        fields = "__all__"


class EmailLoginSerializer(DynamicFieldSerializerMixin, serializers.Serializer):
    """
    Serializer for user email login
    """
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = (
            "email",
            "password",
        )


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login
    """
    EMAIL_LOGIN = "EMAIL_LOGIN"
    LOGIN_TYPES = [EMAIL_LOGIN]

    action = serializers.ChoiceField(required=True, choices=LOGIN_TYPES)
    payload = serializers.DictField(required=True)

    def to_internal_value(self, value):
        login_type = value.get("action")

        if login_type == self.EMAIL_LOGIN:
            self.fields["payload"] = EmailLoginSerializer(data=value.get("payload"))

        return super().to_internal_value(value)


class AddUserSerializer(serializers.Serializer):
    """
    Serializer for add user
    """
    first_name = serializers.CharField(required=False, max_length=200)
    last_name = serializers.CharField(required=False, max_length=200)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    is_staff = serializers.BooleanField(default=False)

    class Meta:
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
        )

    def create(self, validated_data):
        #  function creates user object
        user = User.objects.create(
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_staff=validated_data['is_staff'],
        )
        return user
    
    
class UserUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(max_length=256, required=False)
    last_name = serializers.CharField(max_length=256, required=False)
    phone_code = serializers.CharField(max_length=10, required=False)
    phone_number = serializers.CharField(max_length=20, required=False)
    profile_photo = serializers.CharField(required=False)
    profile_photo_name = serializers.CharField(max_length=100, required=False)

    class Meta:
        fields = "__all__"

class PasswordUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, max_length=15)

    class Meta:
        fields = "__all__"

