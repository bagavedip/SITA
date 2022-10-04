import logging
from sita.models.geolocations import GeoLocation
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)


class GeoLocationService:
    """
     Services for Geolocation models
    """
    
    @staticmethod
    def get_queryset():
        """Function to return all Geo location"""
        return GeoLocation.objects.all()

    @staticmethod
    def get_object_or_404(start_datetime):
        """
        Function which find location by id else raise 404 exception
        """
        logger.info(f"Received Geo Location start datetime {start_datetime}")
        return get_object_or_404(GeoLocationService.get_queryset(), pk=start_datetime)

    @staticmethod
    def location_filter(entity_id):
        """
        Function which extract data of location with filteration of id
        """
        filtered_data = GeoLocationService.get_queryset().filter(entity_id=entity_id)
        return filtered_data

    @staticmethod
    def update(location_data, **kwargs):
        """
        Function update an asset from kwargs
        """
        for key, value in kwargs.items():
            setattr(location_data, key, value)
        location_data.save()

        return location_data
