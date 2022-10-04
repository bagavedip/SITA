from django.conf import settings
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers


class DynamicFieldSerializerMixin:
    """
    Mixin class to use it with serializer for dynamically
    set a field
    """

    def __init__(self, *args, **kwargs):
        """
        Overriding this method to dynamically set fields based on kwarg fields
        """
        # Don't pass the 'fields' arg up to the superclass
        self.whitelisted_fields = kwargs.pop("fields", None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        # Drop any fields that are not specified in the `fields` argument.
        self.whitelist_fields(self.fields)

    def to_representation(self, obj):
        """
        Overrides this method ignore fields added by to_representation
        """
        fields = super().to_representation(obj)
        return self.whitelist_fields(fields)

    def whitelist_fields(self, serializer_fields):
        """
        Function which whitelisted fields based on serializer
        whitelisted_fields
        """
        # Drop any fields that are not specified in the `fields` argument.
        if self.whitelisted_fields:
            for field in set(serializer_fields.keys()):
                if field not in self.whitelisted_fields:
                    serializer_fields.pop(field)

        return serializer_fields


class PasswordField(serializers.CharField):
    """
    Custom Field Serializer for password validation.
    """

    def __init__(self, *args, **kwargs):
        error_message = _("This password is not strong.")
        error_code = "password_is_weak"

        kwargs["required"] = True
        kwargs["write_only"] = True
        kwargs["min_length"] = settings.PASSWORD_MIN_LENGTH
        kwargs["validators"] = [
            RegexValidator(regex=settings.MIN_ONE_CHAR_REGEX, message=error_message, code=error_code),
            RegexValidator(regex=settings.MIN_ONE_SPECIAL_CHAR_REGEX, message=error_message, code=error_code,),
        ]
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return data
