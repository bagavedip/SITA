
import logging

from rest_framework import viewsets
from rest_framework.response import Response
from users.models.preference import Preference
from users.serializers.preference import PreferenceSerializer

from users.services.preference import PreferenceService
logger = logging.getLogger(__name__)


class PreferenceViewSet(viewsets.GenericViewSet):

    def preference_input(self, request):
        try:
            logger.debug(f"Parsed request body {request.data}")
            user_id = request.user.id
            serializer = PreferenceSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            validated_data = serializer.validated_data

            preference = PreferenceService.preference_input(user_id, validated_data)
            logger.debug("Database transaction finished")

            # response formatting
            response_data = {
                "message": f"Preference id {preference} Saved SuccessFully !",
                "status": "success"
                ""
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "message": f"{e}",
                "status": "error"
            }
            return Response(response_data)

    def preference_fetch(self, request):
        try:
            logger.debug(f"Parsed request body {request.data}")
            queryset = Preference.objects.filter(user=request.user.id).values("user","session")
            query = queryset[0]

            return Response(query)
        except Exception as e:
            response_data = {
                "message": f"{e}",
                "status": "error"
            }
            return Response(response_data)