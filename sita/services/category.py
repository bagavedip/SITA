import logging
from sita.models.category import Category
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)


class CategoryService:
    """
     Services for Category models
    """
    
    @staticmethod
    def get_queryset():
        """Function to return all Entity"""
        return Category.objects.all()

    @staticmethod
    def get_object_or_404(start_datetime):
        """
        Function which find Entity by id else raise 404 exception
        """
        logger.info(f"Received Category start datetime {start_datetime}")
        return get_object_or_404(CategoryService.get_queryset(), pk=start_datetime)

    @staticmethod
    def update(category_data, **kwargs):
        """
        Function update an asset from kwargs
        """
        for key, value in kwargs.items():
            setattr(category_data, key, value)
        category_data.save()

        return category_data
