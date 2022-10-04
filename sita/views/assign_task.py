import logging

from django.db import transaction, IntegrityError
from rest_framework import viewsets, status
from rest_framework.response import Response

from sita.serializers.assign_user import AssignUserSerializer
from sita.services.assign_task import AssignTaskService

logger = logging.getLogger(__name__)


class AssignTaskViewset(viewsets.GenericViewSet):

    def assign_user(self, request):
        """
         Function for assign user for selected incident
         in grid views.
        """
        try:
            serializer = AssignUserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            validated_data = serializer.data
            with transaction.atomic():
                selected_incidents = validated_data["selectedIncidents"]
                user_name = validated_data["userName"]
                assign_user = AssignTaskService.assign_user(selected_incidents, user_name)
            logger.debug("Database transaction finished")
            # response formatting
            response_data = {
                "msg": "Comment added successfully !!",
                "status": True
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response("user already assign.")
