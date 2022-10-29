from users.models.preference import Preference


class PreferenceService:

    @staticmethod
    def preference_input(user_id, validated_data):
        Preference.objects.update_or_create(user=user_id, defaults={"session": validated_data.get("session")})
