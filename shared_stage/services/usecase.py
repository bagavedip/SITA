import logging
from shared_stage.models.usecase import UseCase
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)


class UseCaseService:
    
    @staticmethod
    def get_queryset():
        """Function to return all Usecase"""
        return UseCase.objects.all()

    @staticmethod
    def get_object_or_404(start_datetime):
        """
        Function which find Usecase by id else raise 404 exception
        """
        logger.info(f"Received UseCase start datetime {start_datetime}")
        return get_object_or_404(UseCaseService.get_queryset(), pk=start_datetime)
