import logging
from sita.models.process import Process
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)


class ProcessService:
    """
     Services for process models
    """
    
    @staticmethod
    def get_queryset():
        """Function to return all Entity"""
        return Process.objects.all()

    @staticmethod
    def get_object_or_404(start_datetime):
        """
        Function which find Entity by id else raise 404 exception
        """
        logger.info(f"Received Category start datetime {start_datetime}")
        return get_object_or_404(ProcessService.get_queryset(), pk=start_datetime)

    @staticmethod
    def update(process_data, **kwargs):
        """
        Function update an asset from kwargs
        """
        for key, value in kwargs.items():
            setattr(process_data, key, value)
        process_data.save()

        return process_data
