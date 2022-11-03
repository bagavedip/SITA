import logging

from django.core.files.base import ContentFile
from django.utils import timezone

from sita.models.security_pulse import SecurityPulse
from sita.models.security_pulse_image_data import SecurityPulseImage
from sita.serializers.security_pulse_grid import SecurityPulseGridSerializer

logger = logging.getLogger(__name__)


class SecurityPulseService:
    """
    Service for Security Pulse model
    """
    @staticmethod
    def update(asset, **kwargs):
        """
        Function update an asset from kwargs
        """
        for key, value in kwargs.items():
            setattr(asset, key, value)
        asset.save()

        return asset

    @staticmethod
    def create_from_validated_data(user, validated_data):
        """
        Function for creating security pulse with validated data
        """
        sections = validated_data.get("sections")
        security_pulse_kwargs = {
            "criticality_type": validated_data.get("criticality"),
            "security_pulse_title": validated_data.get("securityPulseTitle"),
            "main_title": validated_data.get("mainTitle"),
            "links": validated_data.get("links"),
            "recommendations": validated_data.get("recommendations"),
            "selected_assets": validated_data.get("selectedAssets"),
            "selected_entities": validated_data.get("selectedEntities"),
            "selected_incident": validated_data.get("selectedIncidents"),
            "is_published": validated_data.get("isPublished"),
            "created_by": user,
            "updated_by": user,
            "created_at": timezone.now(),
            "updated_at": timezone.now()
        }
        response = SecurityPulse.objects.create(**security_pulse_kwargs)
        if validated_data.get("sections") is None:
            security_pulse_image_kwargs = {
                "image_data": None,
                "info": None,
                "security_pulse": response

            }
            security_pulse_image = SecurityPulseImage.objects.create(**security_pulse_image_kwargs)
        else:
            for section in sections:
                image_data = section.get("imageData")
                image_data_name = section.get("imageDataName")
                image = None if image_data is None else ContentFile(image_data, name=image_data_name)
                info = section.get("info")
                security_pulse_image_kwargs = {
                    "image_data": image,
                    "info": info,
                    "security_pulse": response

                }
                security_pulse_image = SecurityPulseImage.objects.create(**security_pulse_image_kwargs)
        return response

    @staticmethod
    def security_pulse_grid(response_obj: SecurityPulseGridSerializer):
        """
        Function which fetches security pulse grid
        """
        query_data = SecurityPulse.objects.all().values(*response_obj.select_cols)
        query_data = reversed(query_data)
        return query_data

    @staticmethod
    def delete(security):
        """Function which delete security_pulse.

        Args:
            security ([security_pulse]): [Instance of security_pulse]
        """
        # End date in society
        security.delete()
        logger.info(f"Society with ID {security.pk} deleted successfully.")

    @staticmethod
    def update_from_validated_data(user, validated_data):
        """
        Function which update security pulse with validated data
        """
        securityPulseId = int(validated_data.get("securityPulseId"))
        queryset = SecurityPulse.objects.get(id=securityPulseId)
        sections = validated_data.get("sections")
        security_pulse_kwargs = {
            "criticality_type": validated_data.get("criticality"),
            "security_pulse_title": validated_data.get("securityPulseTitle"),
            "main_title": validated_data.get("mainTitle"),
            "links": validated_data.get("links"),
            "recommendations": validated_data.get("recommendations"),
            "selected_assets": validated_data.get("selectedAssets"),
            "selected_entities": validated_data.get("selectedEntities"),
            "selected_incident": validated_data.get("selectedIncidents"),
            "is_published": validated_data.get("isPublished"),
            "created_by": user,
            "updated_by": user,
            "created_at": timezone.now(),
            "updated_at": timezone.now()
        }
        response = SecurityPulseService.update(queryset, **security_pulse_kwargs)
        if validated_data.get("sections") is None:
            security_pulse_image_kwargs = {
                "image_data": None,
                "info": None,
                "security_pulse": response

            }
            security_pulse_image = SecurityPulseService.update(queryset, **security_pulse_image_kwargs)
        else:
            for section in sections:
                image_data = section.get("imageData")
                image_data_name = section.get("imageDataName")
                image = None if image_data is None else ContentFile(image_data, name=image_data_name)
                info = section.get("info")
                security_pulse_image_kwargs = {
                    "image_data": image,
                    "info": info,
                    "security_pulse": response

                }
            queryset = SecurityPulseImage.objects.filter(security_pulse=securityPulseId)
            if validated_data.get("sections") is not None:
                for query in queryset:
                    security_pulse_image = SecurityPulseService.update(query, **security_pulse_image_kwargs)
        return security_pulse_image

    @staticmethod
    def edit_security_pulse_record_fetch(security_id):
        """
          function to show edit_perspective_record_fetch
          using given id
         """
        queryset = SecurityPulse.objects.get(id=security_id)
        selected_id = queryset.selected_incident
        selected_assets = queryset.selected_assets
        selected_entities = queryset.selected_entities
        query = SecurityPulseImage.objects.filter(security_pulse=security_id)
        section = []
        for query in query:
            image = None if bool(query.image_data) is False else query.image_data.read()
            info = query.info
            image_name = None if bool(query.image_data) is False else str(query.image_data).split('/')[2],
            image_kwargs = {
                "imageData": image,
                "imageDataName": image_name[0],
                "info": info
            }
            section.append(image_kwargs)
        response_data = {
            "securityPulseTitle": queryset.security_pulse_title,
            "mainTitle": queryset.main_title,
            "criticality": queryset.criticality_type,
            "sections": section,
            "recommendations": queryset.recommendations,
            "links": queryset.links,
            "selectedIncidents": selected_id,
            "selectedAssets": selected_assets,
            "selectedEntities": selected_entities,
            "securityPulseId": security_id,
            "isPublished": queryset.is_published
        }
        return response_data

    @staticmethod
    def security_pulse_details_data(security_id):
        """
          function to show edit_perspective_record_fetch
          using given id
         """
        queryset = SecurityPulse.objects.get(id=security_id)
        query = SecurityPulseImage.objects.filter(security_pulse=security_id)
        final_date = queryset.created_at.strftime("%d-%m-%Y")
        if query is None:
            response_data = {
                "headerData": {
                    "user": queryset.created_by.first_name + " " + queryset.created_by.last_name,
                    "designation": queryset.created_by.role_id.name,
                    "createdDate": final_date.strftime("%d-%m-%Y")
                },
                "securityPulseFormData": {
                    "securityPulseTitle": queryset.security_pulse_title,
                    "mainTitle": queryset.main_title,
                    "sections": [],
                    "recommendations": queryset.recommendations,
                    "criticality": queryset.criticality_type,
                    "links": queryset.links,
                    "selectedIncidents": queryset.selected_incident,
                    "selectedAssets": queryset.selected_assets,
                    "selectedEntities": queryset.selected_entities,
                },
                "footerData": {
                    "email": "info@etek.com",
                    "contacts": [
                        {
                            "countryName": "Colombia",
                            "contactNo": "+57(1)2571520"
                        },
                        {
                            "countryName": "Peru'",
                            "contactNo": "+51(1)6124343"
                        },
                        {
                            "countryName": "India",
                            "contactNo": "+91-9873451221"
                        }
                    ]
                }
            }
        else:
            section = []
            for query in query:
                image = None if bool(query.image_data) is False else query.image_data.read()
                info = query.info
                image_name = None if bool(query.image_data) is False else str(query.image_data).split('/')[2],
                image_kwargs = {
                    "imageData": image,
                    "imageDataName": image_name[0],
                    "info": info
                }
                section.append(image_kwargs)
            response_data = {
                "headerData": {
                    "user": queryset.created_by.first_name,
                    "designation": "Cyber Security Engineer",
                    "createdDate": final_date
                },
                "securityPulseFormData": {
                    "securityPulseTitle": queryset.security_pulse_title,
                    "mainTitle": queryset.main_title,
                    "sections": section,
                    "recommendations": queryset.recommendations,
                    "criticality": queryset.criticality_type,
                    "links": queryset.links,
                    "selectedIncidents": queryset.selected_incident,
                    "selectedAssets": queryset.selected_assets,
                    "selectedEntities": queryset.selected_entities,
                },
                "footerData": {
                    "email": "info@etek.com",
                    "contacts": [
                        {
                            "countryName": "Colombia",
                            "contactNo": "+57(1)2571520"
                        },
                        {
                            "countryName": "Peru'",
                            "contactNo": "+51(1)6124343"
                        },
                        {
                            "countryName": "India",
                            "contactNo": "+91-9873451221"
                        }
                    ]
                }
            }
        return response_data
