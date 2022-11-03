import logging
from operator import itemgetter

from django.db.models import Q
from django.utils import timezone
from django.core.files.base import ContentFile
from sita.models.perspective import Perspective
from sita.serializers.perspective_grid_view import PerspectiveGridSerializer

logger = logging.getLogger(__name__)


class PerspectiveService:
    """
     Services for perspective models
    """

    @staticmethod
    def get_queryset():
        """Function to return all Entity"""
        return Perspective.objects.all()

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
    def perspective_dropdown_data():
        """
         function fetch all required data from
         Perspective model for perspective_dropdown_data.
        """
        # fetch perspective_type list in models
        perspective_type = Perspective.objects.values_list('perspective_type').distinct()
        perspective_dropdown = [{
            "label": "Perspective Type",
            "value": "Select"
        }]

        # fetch action_type list in models
        action_type = Perspective.objects.values_list('action_type').distinct()
        action_dropdown = [{
            "label": "Action Taken",
            "value": "Select",
        }]

        # fetch status list in models
        status = Perspective.objects.values_list('status_type').distinct()
        status_dropdown = [{
            "label": "Status",
            "value": "Select"
        }]
        for perspective in perspective_type:
            for per in perspective:
                new_asset = {
                    "label": per,
                    "value": per,
                }

                perspective_dropdown.append(new_asset)
        for action in action_type:
            for act in action:
                new_geo = {
                    "label": act,
                    "value": act
                }
                action_dropdown.append(new_geo)
        for stat in status:
            for i in stat:
                new_entity = {
                    "label": i,
                    "value": i
                }
                status_dropdown.append(new_entity)

        # final response which gives actual dropdown_data
        response = [
            {
                "id": "Perspective Type",
                "dropdownoption": perspective_dropdown
            },
            {
                "id": "Action Taken",
                "dropdownoption": action_dropdown
            },
            {
                "id": "Status",
                "dropdownoption": status_dropdown
            }
        ]
        return response


    @staticmethod
    def create_from_validated_data(user, validated_data):
        """
        Function for creating perspective with validated data
        """
        imageData1 = validated_data.get("imageData1", None)
        imageData2 = validated_data.get("imageData2", None)
        imageData3 = validated_data.get("imageData3", None)
        imageData4 = validated_data.get("imageData4", None)
        imageData1Name = validated_data.get("imageData1Name", None)
        imageData2Name = validated_data.get("imageData2Name", None)
        imageData3Name = validated_data.get("imageData3Name", None)
        imageData4Name = validated_data.get("imageData4Name", None)
        donut_left_graph = None if imageData1 is None else ContentFile(imageData1, name=imageData1Name)
        donut_right_graph = None if imageData2 is None else ContentFile(imageData2, name=imageData2Name)
        comparative_left_graph = None if imageData3 is None else ContentFile(imageData3, name=imageData3Name)
        comparative_right_graph = None if imageData4 is None else ContentFile(imageData4, name=imageData4Name)
        perspective_kwargs = {
            "perspective_type": "Incident" if validated_data.get("selectedPerspectiveFilter") is None else validated_data.get("selectedPerspectiveFilter"),
            "action_type": "no_action" if validated_data.get("selectedActionTakenFilter") is None else validated_data.get("selectedActionTakenFilter"),
            "status_type": "under_investigation" if validated_data.get("selectedActedUponFilter") is None else validated_data.get("selectedActedUponFilter"),
            "criticality_type": "Low" if validated_data.get("selectedLevelFilter") is None else validated_data.get("selectedLevelFilter"),
            "incident_id": validated_data.get("selectedIds",  None),
            "perspective_title": validated_data.get("perspectiveTitle",  None),
            "bar_graph_title": validated_data.get("barGraphTitle",  None),
            "perspective": validated_data.get("perspectiveInput",  None),
            "recommendation": validated_data.get("recomendationsInput",  None),
            "selected_assets": validated_data.get("selectedAssets",  None),
            "selected_entities": validated_data.get("selectedEntities",  None),
            "is_published": validated_data.get("isPublished",  None),
            "donut_left_graph": donut_left_graph,
            "donut_right_graph": donut_right_graph,
            "comparative_left_graph": comparative_left_graph,
            "comparative_right_graph": comparative_right_graph,
            "incident_start_date_time": validated_data.get("startDateTime",  None),
            "incident_end_date_time": validated_data.get("endDateTime",  None),
            "created_by": user,
            "updated_by": user,
            "created_at": timezone.now(),
            "updated_at": timezone.now()
        }
        response = Perspective.objects.create(**perspective_kwargs)
        return response

    @staticmethod
    def update_from_validated_data(user, validated_data):
        """
        Function for updating perspective with validated data
        """
        perspectiveId = int(validated_data.get("perspectiveId"))
        queryset = Perspective.objects.get(id=perspectiveId)
        imageData1 = validated_data.get("imageData1", None)
        imageData2 = validated_data.get("imageData2", None)
        imageData3 = validated_data.get("imageData3", None)
        imageData4 = validated_data.get("imageData4", None)
        imageData1Name = validated_data.get("imageData1Name", None)
        imageData2Name = validated_data.get("imageData2Name", None)
        imageData3Name = validated_data.get("imageData3Name", None)
        imageData4Name = validated_data.get("imageData4Name", None)
        donut_left_graph = None if imageData1 is None else ContentFile(imageData1, name=imageData1Name)
        donut_right_graph = None if imageData2 is None else ContentFile(imageData2, name=imageData2Name)
        comparative_left_graph = None if imageData3 is None else ContentFile(imageData3, name=imageData3Name)
        comparative_right_graph = None if imageData4 is None else ContentFile(imageData4, name=imageData4Name)
        perspective_kwargs = {
            "perspective_type": validated_data.get("selectedPerspectiveFilter", None),
            "action_type": validated_data.get("selectedActionTakenFilter", None),
            "status_type": validated_data.get("selectedActedUponFilter", None),
            "criticality_type": validated_data.get("selectedLevelFilter", None),
            "incident_id": validated_data.get("selectedIds", None),
            "perspective_title": validated_data.get("perspectiveTitle", None),
            "bar_graph_title": validated_data.get("barGraphTitle", None),
            "perspective": validated_data.get("perspectiveInput", None),
            "recommendation": validated_data.get("recomendationsInput", None),
            "selected_assets": validated_data.get("selectedAssets", None),
            "selected_entities": validated_data.get("selectedEntities", None),
            "donut_left_graph": donut_left_graph,
            'donut_right_graph': donut_right_graph,
            "comparative_left_graph": comparative_left_graph,
            "comparative_right_graph": comparative_right_graph,
            "incident_start_date_time": validated_data.get("startDateTime", None),
            "incident_end_date_time": validated_data.get("endDateTime", None),
            "is_published": validated_data.get("isPublished", None),
            "created_by": user,
            "updated_by": user,
            "updated_at": timezone.now()
        }
        logger.debug(f"Updating asset with following kwargs {perspective_kwargs}")
        perspective = PerspectiveService.update(queryset, **perspective_kwargs)
        return perspective

    @staticmethod
    def perspective_details_data(perspective_id):
        """
         function to show perspective_details_data
         using given id
        """
        queryset = Perspective.objects.get(id=perspective_id)
        perspective_title = queryset.perspective_title
        selected_id = queryset.incident_id
        selected_assets = queryset.selected_assets
        selected_entities = queryset.selected_entities
        created_at = queryset.created_at
        created_date = str(created_at)[:10]
        created_time = str(created_at)[11:19]
        updated_at = queryset.updated_at
        updated_date = str(updated_at)[:10]
        updated_time = str(updated_at)[11:19]
        donut_left_graph = None if bool(queryset.donut_left_graph) is False else queryset.donut_left_graph.read()
        donut_right_graph = None if bool(queryset.donut_right_graph) is False else queryset.donut_right_graph.read()
        comparative_left_graph = None if bool(queryset.comparative_left_graph) is False else queryset.comparative_left_graph.read()
        comparative_right_graph = None if bool(queryset.comparative_right_graph) is False else queryset.comparative_right_graph.read()
        response_data = {
            "perspectiveFormData": {
                "perspective_id": perspective_id,
                "perspectiveTitle": perspective_title,
                "selectedIds": selected_id,
                "selectedAssets": selected_assets,
                "selectedEntities": selected_entities,
                "perspectiveInput": queryset.perspective,
                "recomendationsInput": queryset.recommendation,
                "imageData1": donut_left_graph,
                "imageData2": donut_right_graph,
                "imageData3": comparative_left_graph,
                "imageData4": comparative_right_graph,
                "imageData1Name": None if bool(queryset.donut_left_graph) is False else
                str(queryset.donut_left_graph).split('/')[2],
                "imageData2Name": None if bool(queryset.donut_right_graph) is False else
                str(queryset.donut_right_graph).split('/')[2],
                "imageData3Name": None if bool(queryset.comparative_left_graph) is False else
                str(queryset.comparative_left_graph).split('/')[2],
                "imageData4Name": None if bool(queryset.comparative_right_graph) is False else
                str(queryset.comparative_right_graph).split('/')[2],
            },
            "footerData": {
                "lastUpdateInformation": {
                    "user": str(queryset.created_by.first_name) + " " + str(queryset.updated_by.last_name),
                    "date": created_at.date(),
                    "time": created_time
                },
                "originallyCreatedBy": {
                    "user": str(queryset.created_by.first_name) + " " + str(queryset.created_by.last_name),
                    "date": updated_date,
                    "time": updated_time
                }
            }
        }
        return response_data

    @staticmethod
    def edit_perspective_record_fetch(perspective_id):
        """
         function to show edit_perspective_record_fetch
         using given id
        """
        queryset = Perspective.objects.get(id=perspective_id)
        perspective_title = queryset.perspective_title
        selected_id = queryset.incident_id
        selected_assets = queryset.selected_assets
        selected_entities = queryset.selected_entities
        donut_left_graph = None if bool(queryset.donut_left_graph) is False else queryset.donut_left_graph.read()
        donut_right_graph = None if bool(queryset.donut_right_graph) is False else queryset.donut_right_graph.read()
        comparative_left_graph = None if bool(queryset.comparative_left_graph) is False else queryset.comparative_left_graph.read()
        comparative_right_graph = None if bool(queryset.comparative_right_graph) is False else queryset.comparative_right_graph.read()
        response_data = {
                "perspectiveTitle": perspective_title,
                "barGraphTitle": queryset.bar_graph_title,
                "perspectiveInput": queryset.perspective,
                "recomendationsInput": queryset.recommendation,
                "selectedLevelFilter": queryset.criticality_type,
                "selectedActionTakenFilter": queryset.action_type,
                "startDateTime": queryset.incident_start_date_time,
                "endDateTime": queryset.incident_end_date_time,
                "selectedPerspectiveFilter": queryset.perspective_type,
                "selectedActedUponFilter": queryset.status_type,
                "selectedIds": selected_id,
                "selectedAssets": selected_assets,
                "selectedEntities": selected_entities,
                "imageData1": donut_left_graph,
                "imageData2": donut_right_graph,
                "imageData3": comparative_left_graph,
                "imageData4": comparative_right_graph,
                "imageData1Name": None if bool(queryset.donut_left_graph) is False else str(queryset.donut_left_graph).split('/')[2],
                "imageData2Name": None if bool(queryset.donut_right_graph) is False else str(queryset.donut_right_graph).split('/')[2],
                "imageData3Name": None if bool(queryset.comparative_left_graph) is False else str(queryset.comparative_left_graph).split('/')[2],
                "imageData4Name": None if bool(queryset.comparative_right_graph) is False else str(queryset.comparative_right_graph).split('/')[2],
                "perspectiveId": perspective_id,
                "isPublished": queryset.is_published
        }
        return response_data

    @staticmethod
    def perspective_grid(response_obj: PerspectiveGridSerializer):
        """
        Function which fetch perspective grid
        """
        filter_q = Q(**response_obj.filters)
        query_data = None
        if not response_obj.dropdownFilters:
            query_data = Perspective.objects.filter(updated_at__gte=response_obj.start_date, updated_at__lte=response_obj.actual_end_time).values(*response_obj.select_cols)
        else:
            found_filters = {}
            name_replacement_dict = {"Perspective Type": "perspective_type",
                                     "Action Taken": "action_type", "Status": "status_type"}
            for filter_type in response_obj.dropdownFilters:
                if filter_type.get('value') != 'Select':
                    found_filters.update({name_replacement_dict.get(filter_type.get('id')): filter_type.get('value')})
                else:
                    pass
            filter_found = Q(**found_filters)
            query_data = Perspective.objects.filter(updated_at__gte=response_obj.start_date, updated_at__lte=response_obj.actual_end_time).filter(filter_found).values(
                *response_obj.select_cols)
        #query_data = sorted(query_data, key=itemgetter('created_at'), reverse=True)
        return query_data

    @staticmethod
    def delete(perspective):
        """Function which delete perspective.

        Args:
            perspective ([perspective]): [Instance of perspective]
        """
        # End date in society
        perspective.delete()
        logger.info(f"Society with ID {perspective.pk} deleted successfully.")
