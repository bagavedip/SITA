import csv
import codecs
import logging
from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from sita.models.process import Process

from ..models.category import Category

from sita.serializers.assets import AssetSerializer
from sita.services.assets import AssetService
from sita.models.assets import Assets

from django.db import transaction
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location="tmp/")

logger = logging.getLogger(__name__)


class AssetViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = AssetSerializer

    def validated_data(self):
        """
        Function which return validated data
        """
        request_data = self.request.data
        serializer_args = list()
        serializer_kwargs = {"data": request_data}

        if self.action in ["update", "partial_update"]:
            serializer_args.append(self.get_object())

        if self.action in ["partial_update"]:
            serializer_kwargs["partial"] = True

        serializer = self.get_serializer(*serializer_args, **serializer_kwargs)
        serializer.is_valid(raise_exception=True)
        return serializer.validated_data

    @action(detail=False, methods=["post"])
    def addasset(self, request):
        """
         Function to add assets in admin
        """
        if request.method == 'POST':
            Serializer = AssetSerializer(data=request.data)
            data = {}
            if Serializer.is_valid():
                if not AssetService.get_queryset().filter(AssetName__iexact=request.data["AssetName"]).exists():
                    process_query = Process.objects.get(process=request.data["process"])
                    category_query = Category.objects.get(category=request.data["category_name"])
                    asset_list = Assets(
                        AssetName=request.data["AssetName"],
                        category=category_query,
                        process_id=process_query,
                        criticality=request.data["criticality"],
                    )
                    asset_list.save()
                    data['Asset_Name'] = asset_list.AssetName
                    data['Category'] = asset_list.category_id
                    data['Criticality'] = asset_list.criticality
                    data['Process_Id'] = asset_list.process_id_id
                    return Response(
                        {
                            "Status": status.HTTP_200_OK,
                            "Message": "Asset Successfully Added",
                            "Asset_Details": data,
                        }
                    )
                else:
                    return Response(
                        {
                            "Status": status.HTTP_400_BAD_REQUEST,
                            "Message": "Data Already Exist."
                        }
                    )
            else:
                data = Serializer.errors
                return Response(
                    {
                        "Status": status.HTTP_204_NO_CONTENT,
                        "Message": "Fill required data",
                        "Asset_Details": data
                    }
                )

    @action(detail=False, methods=['POST'])
    def validate_asset_csv(self, request):
        """
        Function to validate asset csv file.
        """
        file = request.FILES.get("File")
        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)
        serializer = AssetSerializer(data=data, many=True)
        if serializer.is_valid():
            return Response({
                "Status": status.HTTP_200_OK,
                "Message": "Validation Successful",
                "Data": data
            }
            )
        else:
            asset_err = serializer.errors
            return Response({
                "Status": status.HTTP_406_NOT_ACCEPTABLE,
                "Message": serializer.errors,
                "Data": asset_err
            }
            )

    @action(detail=False, methods=['POST'])
    def upload_asset(self, request):
        """
        Upload data from CSV, with validation.
        """
        file = request.FILES.get("File")

        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)
        serializer = AssetSerializer(data=data, many=True)
        if serializer.is_valid():
            asset_list = []
            for row in serializer.data:
                category_queryset = Category.objects.get(category=row["category_name"])
                process_queryset = Process.objects.get(process=row["process"])
                asset_list.append(
                    Assets(
                        AssetName=row["AssetName"],
                        category=category_queryset,
                        criticality=row["criticality"],
                        process_id=process_queryset,
                    )
                )
            Assets.objects.bulk_create(asset_list)

            return Response({
                "Status": status.HTTP_200_OK,
                "Message": "Successfully upload the data",
                "Data": data
            }
            )
        else:
            asset_err = serializer.errors
            return Response({
                "Status": status.HTTP_406_NOT_ACCEPTABLE,
                "Message": serializer.errors,
                "Data": asset_err
            }
            )

    def asset(self, request):
        """
         Function returns asset record.
        """
        logger.info(f"request data is{request.data}")
        queryset = AssetService.get_queryset().filter(end_date__isnull = True).select_related('process_id', 'process_id__function_id','process_id__function_id__location_id',
                                                              'process_id__function_id__location_id__entity_id')
        total_assets = []
        for asset in queryset:
            data = ({
                "id": asset.id,
                "Asset_Name": asset.AssetName,
                "Category": asset.category.category,
                "Criticality": asset.criticality,
                "Process_Name": asset.process_id.process,
                "Function_Name": asset.process_id.function_id.function_name,
                "Location": asset.process_id.function_id.location_id.location,
                "Entity": asset.process_id.function_id.location_id.entity_id.entityname,
                "Created_date": asset.created,
            })

            total_assets.append(data)
        return Response(
            {
                "Status": "Success",
                "Data": total_assets,
            }
        )

    def single_asset(self, request, asset_id):
        """
         Function used for details of single asset
        """
        logger.info(f"request data is{request.data}")
        queryset = AssetService.get_queryset().filter(id=asset_id).select_related('category', "process_id",'process_id__function_id',
                                                                                  'process_id__function_id__location_id',
                                                                                  'process_id__function_id__location_id__entity_id')
        Total_assets = []
        for asset in queryset:
            data = ({
                "id": asset.id,
                "Asset_Name": asset.AssetName,
                "Category": asset.category.category,
                "Criticality": asset.criticality,
                "Process_Name": asset.process_id.process,
                "Function_Name": asset.process_id.function_id.function_name,
                "Location": asset.process_id.function_id.location_id.location,
                "Entity": asset.process_id.function_id.location_id.entity_id.entityname,
                "Created_date": asset.created,
            })

            Total_assets.append(data)
        return Response(
            {
                "Status": "Success",
                "Data": Total_assets,
            }
        )

    @action(detail=False, methods=["put"])
    def update_asset(self, request, asset):
        """
            Function to update asset queryset
        """
        serializer = AssetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            category_queryset = Category.objects.get(category=request.data["category_name"])
            process_queryset = Process.objects.get(process=request.data["process"])
            valid_data = {
                "AssetName": request.data["AssetName"],
                "category": category_queryset,
                "process_id": process_queryset,
                "criticality": request.data["criticality"]
            }

            asset_query = AssetService.get_queryset().filter(id=asset)
            for asset in asset_query:
                assets = AssetService.update(asset, **valid_data)
                data = {
                    "id": assets.pk,
                    "Asset Name": assets.AssetName,
                }
        return Response(data)

    def asset_delete(self, request, asset_id):
        """
         Function used to delete an asset record.
        """
        logger.info(f"request data is {request.data}")
        queryset = Assets.objects.get(id=asset_id)
        if queryset:
            queryset.end_date = datetime.now()
            queryset.save()
            message = f"Record deleted for id {asset_id}"
            Status = status.HTTP_200_OK
        else:
            message = f"Record not found for id {asset_id}"
            Status = status.HTTP_404_NOT_FOUND
        return Response(
            {
                "Status": Status,
                "Message": message
            })
