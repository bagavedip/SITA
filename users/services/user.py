import logging
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)
User = get_user_model()


class UserService:
    """
    Services for user model
    """

    @staticmethod
    def get_queryset():
        queryset = User.objects.all()
        return queryset

    def get_user_queryset(self):
        return UserService.get_queryset()

    @staticmethod
    def active():
        """
        function fetch active users only
        """
        queryset = UserService.get_queryset().filter(is_active=True)
        return queryset

    @staticmethod
    def update(user, validated_data):
        """
        Function which updates a user info
        """
        logger.info(f"Received validated data {validated_data}")
        user_kwargs = {
            "first_name": validated_data.get("first_name", user.first_name),
            "last_name": validated_data.get("last_name", user.last_name),
            "email": validated_data.get("email", user.email),
        }
        logger.debug(f"Updating user emergency contact with following kwargs {user_kwargs}")
        user_info = user
        for attr, value in user_kwargs.items():
            setattr(user_info, attr, value)
        user_info.save()
        logger.info(f"User with id {user_info.pk} updated.")
        return user_info

    def get_active_user_by_email(self, email):
        """
        Function to fetch active user email in model
        """
        try:
            email = email.lower()
            queryset = self.get_user_queryset().get(email=email, is_active=True)
            return queryset
        except User.DoesNotExist:
            return None

