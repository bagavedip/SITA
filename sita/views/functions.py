import csv
import codecs
import logging
from datetime import datetime

from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models.geolocations import GeoLocation
from ..models.functions import Function
from sita.serializers.functions import FunctionSerializer
from sita.services.functions import FunctionService
from sita.services.process import ProcessService


logger = logging.getLogger(__name__)


class FunctionViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = FunctionSerializer

    def function(self, request):
        """
         function to get details of function
        """
        logger.info(f"request data is {request.data}")
        queryset = FunctionService.get_queryset()
        dataset = []
        for functions in queryset:
            data = ({
                "Function_id": functions.id,
                "Function_name": functions.function_name,
                "Location_id": functions.location_id.id,
                "Location": functions.location_id.location
            })
            dataset.append(data)
        return Response(
            {
                "Status": status.HTTP_200_OK,
                "Data": dataset,
            }
        )

    def single_function_details(self, request, function_id):
        """
         function to get single record of function
        """
        logger.info(f"request data is {request.data}")
        queryset = FunctionService.get_queryset().filter(id=function_id)
        if queryset:
            queryset_details = []
            for functions in queryset:
                query_data = ({
                    "Function_id": functions.id,
                    "Function_name": functions.function_name,
                    "Location_id": functions.location_id.id,
                    "Location": functions.location_id.location
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

    @action(detail=False, methods=['POST'])
    def validate_function_csv(self, request):
        """
         function to validate csv file of function
        """
        logger.info(f"request data is {request.data}")
        # Upload data from CSV, with validation.
        file = request.FILES.get("File")
        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)
        serializer = FunctionSerializer(data=data, many=True)
        if serializer.is_valid():
            return Response({
                "Status": status.HTTP_200_OK,
                "Message": "Validation Successful",
                "Data": data
            }
            )
        else:
            cate_data = serializer.errors
            return Response({
                "Status": status.HTTP_406_NOT_ACCEPTABLE,
                "Message": serializer.errors,
                "Data": cate_data
            }
            )

    @action(detail=False, methods=['POST'])
    def upload_function(self, request):
        """
        Upload data from CSV, with validation.
        """
        logger.info(f"request data is {request.data}")
        file = request.FILES.get("File")

        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)
        serializer = FunctionSerializer(data=data, many=True)
        if serializer.is_valid():
            function_list = []
            for row in serializer.data:
                location_queryset = GeoLocation.objects.get(location=row["location_name"])
                function_list.append(
                    Function(
                        function_name=row["function_name"],
                        location_id=location_queryset,
                    )
                )
            Function.objects.bulk_create(function_list)

            return Response({
                "Status": status.HTTP_200_OK,
                "Message": "Successfully upload the data",
                "Data": data
            }
            )
        else:
            cate_data = serializer.errors
            return Response({
                "Status": status.HTTP_406_NOT_ACCEPTABLE,
                "Message": serializer.errors,
                "Data": cate_data
            }
            )

    def functionlocationentity(self, request):
        """
         function to get combine details of function, location and entity
        """
        logger.info(f"request data is {request.data}")
        try:
            id = request.query_params["id"]
            if id != None:
                queryset = FunctionService.get_queryset().filter(end_date__isnull = True).select_related('location_id',
                                                                         'location_id__entity_id').filter(id=id)
                dataset = []
                for functions in queryset:
                    data = ({
                        "Function_id": functions.id,
                        "Function_name": functions.function_name,
                        "Location_id": functions.location_id.id,
                        "Location": functions.location_id.location,
                        "Entity_id": functions.location_id.entity_id.id,
                        "Entity": functions.location_id.entity_id.entityname,
                    })
                    dataset.append(data)
                return Response(
                    {
                        "Status": status.HTTP_200_OK,
                        "Data": dataset,
                    }
                )
            else:
                return Response(
                    {
                        "Status": status.HTTP_400_BAD_REQUEST,
                        "Message": "Please Provide an Id",
                    }
                )
        except:
            queryset = FunctionService.get_queryset().select_related('location_id', 'location_id__entity_id')
            dataset = []
            for functions in queryset:
                data = ({
                    "Function_id": functions.id,
                    "Function_name": functions.function_name,
                    "Location_id": functions.location_id.id,
                    "Location": functions.location_id.location,
                    "Entity_id": functions.location_id.entity_id.id,
                    "Entity": functions.location_id.entity_id.entityname,
                })
                dataset.append(data)
            return Response(
                {
                    "Status": status.HTTP_200_OK,
                    "Data": dataset,
                }
            )

    @action(detail=False, methods=["put"])
    def update_function(self, request, function_id):
        """
            Function to update function queryset
        """
        logger.info(f"request data is {request.data}")
        serializer = FunctionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            location_queryset = GeoLocation.objects.get(location=request.data["location_name"])
            valid_data = {
                "function_name": request.data["function_name"],
                "location_id": location_queryset,
            }

            Function_queryset = FunctionService.get_queryset().filter(id=function_id)
            for data in Function_queryset:
                function = FunctionService.update(data, **valid_data)
                data = {
                    "id": function.pk,
                    "Function Name": function.function_name,
                }
        return Response(data)

    def function_delete(self, request, function_id):
        """
         function to delete function
        """
        logger.info(f"request data is {request.data}")
        process_queryset = ProcessService.get_queryset.filter(function_id = function_id)
        if process_queryset:
            message = f"Process is connected to this Function {function_id}"
            Status = status.HTTP_405_METHOD_NOT_ALLOWED
        else:
            queryset = Function.objects.get(id=function_id)
            if queryset:
                queryset.end_date = datetime.now()
                queryset.save()
                message = f"Record deleted for id {function_id}"
                Status = status.HTTP_200_OK
            else:
                message = f"Record not found for id {function_id}"
                Status = status.HTTP_404_NOT_FOUND
        return Response(
            {
                "Status": Status,
                "Message": message
            })

    @action(detail=False, methods=["post"])
    def addfunction(self, request):
        """
         function to add details of function
        """
        logger.info(f"request data is {request.data}")
        if request.method == 'POST':
            Serializer = self.serializer_class(data=request.data)
            data = {}
            if Serializer.is_valid():
                if not FunctionService.get_queryset().filter(function_name__iexact=request.data["function_name"]).exists():
                    location_queryset = GeoLocation.objects.get(location=request.data["location_name"])
                    function_list = Function(
                        function_name=request.data["function_name"],
                        location_id=location_queryset
                    )
                    function_list.save()
                    data["Id"] = function_list.id
                    data['Function'] = function_list.function_name
                    data['Location'] = function_list.location_id_id
                    return Response(
                        {
                            "Status": status.HTTP_200_OK,
                            "Message": "Function Successfully Added",
                            "Data": data
                        }
                    )
                else:
                    return Response(
                        {
                            "Status": status.HTTP_400_BAD_REQUEST,
                            "Message": "Function already Exist",
                        }
                    )
            else:
                data = Serializer.errors
                return Response(
                    {
                        "Status": status.HTTP_204_NO_CONTENT,
                        "Message": "Fill required data",
                        "Function_Details": data
                    }
                )
