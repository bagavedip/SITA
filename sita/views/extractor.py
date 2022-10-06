import datetime
import time

from django.http import HttpResponse
from requests import Response
from rest_framework import viewsets
import logging
from sita.services.extractor_itsm import ITSMServices
from sita.services.extractor_siem import SiemService
from sita.services.extractor_soar import SoarService

logger = logging.getLogger(__name__)


class Extractor(viewsets.GenericViewSet):
    def itsm(self, request, *args, **kwargs):
        """
         Timeline view for insights
        """
        logger.info(f"request data is{request.data}")
        result = ITSMServices.itsm_dump()
        return HttpResponse({
                "Message": "Data Already Exist."}
        )

    def soar(self, request):
        result = SoarService.get_all_cases()
        return HttpResponse("hello")

    def siem(self, request):
        try:
            result = SiemService.qradar()
            return HttpResponse("hello")
        except Exception as e:
            return Response(e)
