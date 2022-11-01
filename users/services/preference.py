from users.models.preference import Preference


class PreferenceService:

    @staticmethod
    def preference_input(user_id, validated_data):
        default_preference = {
                                "oei": {
                                    "day_filter": "1 Day"
                                },
                                "insights": {
                                    "day_filter": "1 Day"
                                },
                                "perspective": {
                                    "day_filter": "1 Day"
                                }
                            }
        if validated_data.get("session") is None:
            Preference.objects.update_or_create(user_id=user_id, defaults={"session": default_preference})
        else:
            Preference.objects.update_or_create(user=user_id, defaults={"session": validated_data.get("session")})
