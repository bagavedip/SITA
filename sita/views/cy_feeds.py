import logging

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from sita.services.cy_feeds import Cy_FeedsService

logger = logging.getLogger(__name__)


class CyFeeds(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]

    def all_feeds(self, request):
        """View Function to extract feeds"""

        # calling services for CY data
        cy_response = Cy_FeedsService.get_cy_feeds()
        return cy_response
