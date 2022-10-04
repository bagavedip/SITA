import logging
from sita.models.assets import Assets
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)


class AssetService:
    """
    Service class for Assets model.
    """

    @staticmethod
    def get_queryset():
        return Assets.objects.all()

    @staticmethod
    def get_object_or_404(start_datetime):
        """
        Function which find asset by id else raise 404 exception
        """
        logger.info(f"Received SIEM start datetime {start_datetime}")
        return get_object_or_404(AssetService.get_queryset(), pk=start_datetime)

    @staticmethod
    def asset_filter(asset_id):
        """
        function which extract asset data on location id 
        """
        filtered_data = AssetService.get_queryset().filter(function_id=asset_id)
        return filtered_data

    @staticmethod
    def update(asset, **kwargs):
        """
        Function update an asset from kwargs
        """
        for key, value in kwargs.items():
            setattr(asset, key, value)
        asset.save()

        return asset
