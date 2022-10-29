import logging
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from sita.services.dashboard import DashboardService

logger = logging.getLogger(__name__)


class DashboardViewSet(viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated]

    def dashboard_grid_data(self, request):
        """
         function to check last three record according last_updated date on
         dashboard
        """
        logger.debug(f"Received request body {request.data}")
        data = DashboardService.dashboard_grid_data()
        return Response(data, status=status.HTTP_200_OK)
