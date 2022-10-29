from django.http import HttpResponse
from requests import Response
from rest_framework import viewsets
import logging
from sita.services.fact import FACTService

logger = logging.getLogger(__name__)


class Fact(viewsets.GenericViewSet):

    def fact(self, request):
        result = FACTService.fact()
        return HttpResponse("hello")

