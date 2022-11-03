import csv
import codecs
import logging
from datetime import datetime

from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from sita.services.geolocations import GeoLocationService
from sita.serializers.entity import EntitySerializer
from sita.models.entity import Entity
from sita.services.entity import EntityService

logger = logging.getLogger(__name__)


class EntityViewSet(viewsets.ModelViewSet):
    """
    Function for handling entities
    """
    permission_classes = [IsAuthenticated]
    serializer_class = EntitySerializer

    # queryset = EntityService.get_queryset()

    def entities(self, request):
        """
         Function to get details of entity.
        """
        logger.info(f"request data is {request.data}")
        queryset = EntityService.get_queryset().filter(end_date__isnull=True)
        dataset = []
        for entity in queryset:
            data = ({
                "id": entity.id,
                "entityname": entity.entityname
            })
            dataset.append(data)
        return Response(
            {
                "Status": status.HTTP_200_OK,
                "Data": dataset,
            }
        )

    def single_entities(self, request, entity_id):
        """
         Function to get details of single entity.
        """
        logger.info(f"request data is {request.data}")
        queryset = EntityService.get_queryset().filter(id=entity_id)
        dataset = []
        if queryset:
            for entity in queryset:
                data = ({
                    "id": entity.id,
                    "entityname": entity.entityname
                })
                dataset.append(data)
        return Response(
            {
                "Status": status.HTTP_200_OK,
                "Data": dataset,
            }
        )

    @action(detail=False, methods=["post"])
    def addentity(self, request):
        """
        Function to add entity details
        """
        logger.info(f"request data is {request.data}")
        if request.method == 'POST':
            Serializer = EntitySerializer(data=request.data)
            data = {}
            if Serializer.is_valid():
                if not EntityService.get_queryset().filter(entityname__iexact=request.data["entityname"]).exists():
                    entity = Serializer.save()
                    data["Id"] = entity.id
                    data['Entity'] = entity.entityname
                    return Response(
                        {
                            "Status": status.HTTP_200_OK,
                            "Message": "Entity Successfully Added",
                            "Process_details": data
                        }
                    )
                else:
                    return Response(
                        {
                            "Status": status.HTTP_400_BAD_REQUEST,
                            "Message": "Entity allready Exist",
                        }
                    )
            else:
                data = Serializer.errors
                return Response(
                    {
                        "Status": status.HTTP_204_NO_CONTENT,
                        "Message": "Fill required data",
                        "Entity_Details": data
                    }
                )

    @action(detail=False, methods=['POST'])
    def validate_entity(self, request):
        """
         Function to validate csv file of entity
        """
        logger.info(f"request data is {request.data}")
        file = request.FILES.get("File")

        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)
        serializer = EntitySerializer(data=data, many=True)
        if serializer.is_valid():
            return Response({
                "Status": status.HTTP_200_OK,
                "Message": "Validation Successful",
                "Data": data
            }
            )
        else:
            entity_err = serializer.errors
            return Response({
                "Status": status.HTTP_406_NOT_ACCEPTABLE,
                "Message": serializer.errors,
                "Data": entity_err
            }
            )

    @action(detail=False, methods=['POST'])
    def upload_entity(self, request):
        """
        Upload data from CSV, with validation.
        """
        logger.info(f"request data is {request.data}")
        file = request.FILES.get("File")

        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)
        serializer = EntitySerializer(data=data, many=True)
        if serializer.is_valid():
            entity_list = []
            for row in serializer.data:
                entity_list.append(
                    Entity(
                        entityname=row["entityname"],
                    )
                )
            Entity.objects.bulk_create(entity_list)

            return Response({
                "Status": status.HTTP_200_OK,
                "Message": "Successfully upload the data",
                "Data": data
            }
            )
        else:
            entity_err = serializer.errors
            return Response({
                "Status": status.HTTP_406_NOT_ACCEPTABLE,
                "Message": serializer.errors,
                "Data": entity_err
            }
            )

    @action(detail=False, methods=["put"])
    def update_entity(self, request, entity_id):
        """
            Function to update entity queryset
        """
        logger.info(f"request data is {request.data}")
        serializer = EntitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        with transaction.atomic():
            Entity_queryset = EntityService.get_queryset().filter(id=entity_id)
            for data in Entity_queryset:
                entity = EntityService.update(data, **validated_data)
                data = {
                    "id": entity.pk,
                    "Entity Name": entity.entityname,
                }
        return Response(data)

    def entity_delete(self, request, entity_id):
        """
         Function to delete entity
        """
        logger.info(f"request data is {request.data}")
        location_queryset = GeoLocationService.get_queryset.filetr(entity_id=entity_id)
        if location_queryset:
            Status = status.HTTP_405_METHOD_NOT_ALLOWED
            message = f"Location is connected to this Entity {entity_id}"
        else:
            queryset = Entity.objects.get(id=entity_id)
            if queryset:
                queryset.end_date = datetime.now()
                queryset.save()
                message = f"Record deleted for id {entity_id}"
                Status = status.HTTP_200_OK
            else:
                message = f"Record not found for id {entity_id}"
                Status = status.HTTP_404_NOT_FOUND
        return Response(
            {
                "Status": Status,
                "Message": message
            })
