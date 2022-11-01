import logging

from django.db import transaction
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from sita.models.security_pulse import SecurityPulse
from sita.serializers.security_pulse_grid import SecurityPulseGridSerializer
from sita.services.perspective import PerspectiveService
from sita.services.security_pulse import SecurityPulseService

logger = logging.getLogger(__name__)


class SecurityPulseViewSet(viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated]

    def add_security_pulse_record(self, request):
        try:
            logger.info("Validating data for Log In.")
            validated_data = request.data
            logger.info("Initiating Log in.")
            login_user = request.user
            with transaction.atomic():
                perspective = SecurityPulseService.create_from_validated_data(login_user, validated_data)
            logger.debug("Database transaction finished")

            # response formatting
            response_data = {"id": perspective.pk}
            return Response({"message": f"perspective with {response_data} created successfully",
                            "status": "success"})
        except Exception as e:
            return Response({"message": f"{e}", "status": "error"})

    def security_pulse_record_delete(self, request):
        """[action to destory society]

        Args:
            request ([Request]): [Django Request instance]
        """
        try:
            login_user = request.user
            security_pulse_id = request.data.get("id")
            queryset = SecurityPulse.objects.get(id=security_pulse_id)
            with transaction.atomic():
                PerspectiveService.delete(queryset)
                response_data = {
                    "message": f"Record {security_pulse_id} Deleted SuccessFully !",
                    "status": "success"
                }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "message": "Error while deleting record",
                "status": "error"
            }
            return Response(response_data)

    def security_pulse_grid_data(self, request):
        """
         function define for security pulse grid data
        """
        try:
            logger.debug(f"Received request body {request.data}")

            response_obj = SecurityPulseGridSerializer(request)

            data = SecurityPulseService.security_pulse_grid(response_obj)
            return Response(response_obj.get_response(data), status=status.HTTP_200_OK)
        except Exception as e:
            response_data = f"e"
        return Response({"message": response_data, "status": "error"})

    def edit_security_pulse_record_submit(self, request):
        """
        Function which update asset information.
        """
        try:
            logger.debug(f"Parsed request body {request.data}")
            login_user = request.user
            validated_data = request.data
            logger.debug(f"Data after validation {validated_data}")

            # update asset and asset user information
            logger.debug("Database transaction started")
            with transaction.atomic():
                asset = SecurityPulseService.update_from_validated_data(login_user, validated_data)
            logger.debug("Database transaction finished")

            # response formatting
            response_data = {
                "message": "Record Updated SuccessFully !",
                "status": "success"
            }
            return Response(response_data)
        except Exception as e:
            response_data = {
                "message": f"{e}",
                "status": "error"
            }
            return Response(response_data)

    def edit_security_pulse_record_fetch(self, request):
        """
         Function define for  edit security pulse record fetch
        """
        try:
            perspective_id = request.data.get("id")
            perspective = SecurityPulseService.edit_security_pulse_record_fetch(perspective_id)
            return Response(perspective)
        except Exception as e:
            response_data = f"{e}"
            return Response({"message": response_data, "status": "error"})

    def security_pulse_details_data(self, request):
        """
         Function define for security pulse details data
        """
        try:
            perspective_id = request.data.get("id")
            perspective = SecurityPulseService.security_pulse_details_data(perspective_id)
            return Response(perspective)
        except Exception as e:
            response_data = f"{e}"
            return Response({"message": response_data, "status": "error"})
