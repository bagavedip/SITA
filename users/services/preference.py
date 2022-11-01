from django.utils import timezone

from users.models.preference import Preference


class PreferenceService:
    """

    """
    @staticmethod
    def preference_input(user_id, validated_data):
        """
        Service for updating User's preference
        """
        preference = Preference.objects.update(user=user_id, session=validated_data.get("session"),
                                               updated_at=timezone.now())
        return preference
