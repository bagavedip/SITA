import csv
import codecs
import logging
from datetime import datetime

from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from sita.models.process import Process
from sita.models.functions import Function
from sita.serializers.process import ProcessSerializer
from sita.services.process import ProcessService
from sita.services.assets import AssetService

logger = logging.getLogger(__name__)


class ProcessViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = ProcessSerializer

    @action(detail=False, methods=["put"])
    def update_process(self, request, process_id):
        """
         function to update details of process
        """
        logger.info(f"request data is {request.data}")
        serializer = ProcessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            function_queryset = Function.objects.get(function_name=request.data["function_name"])
            valid_data = {
                "process": request.data["process"],
                "function_id": function_queryset
            }
            process_queryset = ProcessService.get_queryset().filter(id=process_id)
            for data in process_queryset:
                process = ProcessService.update(data, **valid_data)
                data = {
                    "id": process.pk,
                    "Process Name": process.process,
                }
        return Response(data)

    def process_delete(self, request, process_id):
        """
         function to delete details of process
        """
        logger.info(f"request data is {request.data}")
        asset_queryset = AssetService.get_queryset().filter(process_id=process_id)
        if asset_queryset:
            message = f"Asset is connected to this Procees {process_id}"
            Status = status.HTTP_405_METHOD_NOT_ALLOWED
        else:
            queryset = Process.objects.get(id=process_id)
            if queryset:
                queryset.end_date = datetime.now()
                queryset.save()
                message = f"Record deleted for id {process_id}"
                Status = status.HTTP_200_OK
            else:
                message = f"Record not found for id {process_id}"
                Status = status.HTTP_404_NOT_FOUND
        return Response(
            {
                "Status": Status,
                "Message": message
            })

    @action(detail=False, methods=["post"])
    def addprocess(self, request):
        """
         function to add details of process
        """
        logger.info(f"request data is {request.data}")
        if request.method == 'POST':
            Serializer = ProcessSerializer(data=request.data)
            data = {}
            if Serializer.is_valid():
                if not ProcessService.get_queryset().filter(process__iexact=request.data["process"]).exists():
                    function_queryset = Function.objects.get(function_name=request.data["function_name"])
                    process_list = Process(
                        process=request.data["process"],
                        function_id=function_queryset
                    )
                    process_list.save()
                    data["Id"] = process_list.id
                    data['Process'] = process_list.process
                    data['Function'] = process_list.function_id_id
                    return Response(
                        {
                            "Status": status.HTTP_200_OK,
                            "Message": "Process Successfully Added",
                            "Process_details": data
                        }
                    )
                else:
                    return Response(
                        {
                            "Status": status.HTTP_400_BAD_REQUEST,
                            "Message": "Process already Exist",
                        }
                    )
            else:
                data = Serializer.errors
                return Response(
                    {
                        "Status": status.HTTP_204_NO_CONTENT,
                        "Message": "Fill required data",
                        "Process_Details": data
                    }
                )

    @action(detail=False, methods=['POST'])
    def validate_process(self, request):
        """
         function to validate csv file of process
        """
        logger.info(f"request data is {request.data}")
        # Upload data from CSV, with validation.
        file = request.FILES.get("File")

        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)

        serializer = ProcessSerializer(data=data, many=True)
        if serializer.is_valid():
            return Response({
                "Status": status.HTTP_200_OK,
                "Message": "Validation Successful",
                "Data": data
            }
            )
        else:
            process_err = serializer.errors
            return Response({
                "Status": status.HTTP_406_NOT_ACCEPTABLE,
                "Message": serializer.errors,
                "Data": process_err
            }
            )

    @action(detail=False, methods=['POST'])
    def upload_process(self, request):
        """
         function to upload csv file of process
        """
        logger.info(f"request data is {request.data}")
        file = request.FILES.get("File")

        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)
        serializer = ProcessSerializer(data=data, many=True)
        if serializer.is_valid():
            process_list = []
            for row in serializer.data:
                function_queryset = Function.objects.get(function_name=row["function_name"])
                process_list.append(
                    Process(
                        process=row["process"],
                        function_id=function_queryset
                    )
                )
            Process.objects.bulk_create(process_list)

            return Response({
                "Status": status.HTTP_200_OK,
                "Message": "Successfully upload the data",
                "Data": data
            }
            )
        else:
            process_err = serializer.errors
            return Response({
                "Status": status.HTTP_406_NOT_ACCEPTABLE,
                "Message": serializer.errors,
                "Data": process_err
            }
            )

    def process_details(self, request):
        """
         function to get details of process
        """
        logger.info(f"request data is {request.data}")
        queryset = ProcessService.get_queryset().filter(end_date__isnull=True)
        queryset_details = []
        for data in queryset:
            query_data = ({
                "Id": data.id,
                "Process": data.process,
                "Function_id": data.function_id.id,
                "Function_name": data.function_id.function_name,
                "Location_id": data.function_id.location_id.id,
                "Location": data.function_id.location_id.location,
                "Entity_id": data.function_id.location_id.entity_id.id,
                "Entity": data.function_id.location_id.entity_id.entityname,
            })
            queryset_details.append(query_data)

        return Response(
            {
                "Status": status.HTTP_200_OK,
                "Data": queryset_details
            }
        )

    def single_process_details(self, request, process_id):
        """
         function to get details of single record of process
        """
        logger.info(f"request data is {request.data}")
        queryset = ProcessService.get_queryset().filter(id=process_id)
        if queryset:
            queryset_details = []
            for data in queryset:
                query_data = ({
                    "Id": data.id,
                    "Process": data.process,
                    "Function_id": data.function_id.id,
                    "Function_name": data.function_id.function_name
                })
                queryset_details.append(query_data)

            return Response(
                {
                    "Status": status.HTTP_200_OK,
                    "Data": queryset_details
                }
            )
        else:
            return Response({
                "Status": status.HTTP_404_NOT_FOUND,
                "Message": "Data Not Existing"
            }
            )
