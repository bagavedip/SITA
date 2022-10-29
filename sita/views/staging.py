from django.http import HttpResponse
from requests import Response
from rest_framework import viewsets
import logging
from sita.services.stg_siem import SiemService
from sita.services.stg_itsm import ITSMServices
from sita.services.stg_soar import SoarService

logger = logging.getLogger(__name__)


class Staging(viewsets.GenericViewSet):

    def stg_siem(self, request):
        result = SiemService.qradar()
        return HttpResponse("hello")

    def stg_itsm(self, request):
        result = ITSMServices.itsm()
        return HttpResponse("hello")

    def stg_soar(self, request):
        result = SoarService.soar()
        print('result is', result)
        return HttpResponse("Hello")
      
