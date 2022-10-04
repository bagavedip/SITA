import logging
from sita.models.entity import Entity
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)


class EntityService:
    """
     Services for Entity models
    """
    
    @staticmethod
    def get_queryset():
        """Function to return all Entity"""
        return Entity.objects.all()

    @staticmethod
    def get_object_or_404(start_datetime):
        """
        Function which find Entity by id else raise 404 exception
        """
        logger.info(f"Received Entity start datetime {start_datetime}")
        return get_object_or_404(EntityService.get_queryset(), pk=start_datetime)

    @staticmethod
    def update(entity, **kwargs):
        """
        Function update an asset from kwargs
        """
        for key, value in kwargs.items():
            setattr(entity, key, value)
        entity.save()

        return entity
