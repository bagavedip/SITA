import logging
from shared_stage.models.rules import Rule
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)


class RulesService:
    
    @staticmethod
    def get_queryset():
        """Function to return all Rules"""
        return Rule.objects.all()

    @staticmethod
    def get_object_or_404(start_datetime):
        """
        Function which find Rules by id else raise 404 exception
        """
        logger.info(f"Received Rules start datetime {start_datetime}")
        return get_object_or_404(RulesService.get_queryset(), pk=start_datetime)
