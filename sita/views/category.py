import csv
import codecs
import logging
from datetime import datetime

from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from sita.models.category import Category
from sita.services.assets import AssetService
from sita.serializers.category import CategorySerializer
from sita.services.category import CategoryService

logger = logging.getLogger(__name__)


class CategoryViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer

    @action(detail=False, methods=["post"])
    def addcategory(self, request):
        """
         Function is used to add category in admin
        """
        if request.method == 'POST':
            serializer = CategorySerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                if not CategoryService.get_queryset().filter(category__iexact=request.data["category"]).exists():
                    category = serializer.save()
                    data['Id'] = category.id
                    data['Category'] = category.category
                    return Response(
                        {
                            "Status": status.HTTP_200_OK,
                            "Message": "Category Successfully Added",
                            "Category_details": data
                        }
                    )
                else:
                    return Response(
                        {
                            "Status": status.HTTP_400_BAD_REQUEST,
                            "Message": "Category already Exists",
                        }
                    )
            else:
                data = serializer.errors
                return Response(
                    {
                        "Status": status.HTTP_204_NO_CONTENT,
                        "Message": "Fill required data",
                        "Category_Details": data
                    }
                )

    @action(detail=False, methods=['POST'])
    def validate_category(self, request):
        """
            function to used validate csv file of category.
        """
        file = request.FILES.get("File")
        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)
        serializer = CategorySerializer(data=data, many=True)
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
    def upload_category(self, request):
        """
         Upload data from CSV, with validation.
        """
        file = request.FILES.get("File")

        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)
        serializer = CategorySerializer(data=data, many=True)
        if serializer.is_valid():
            category_list = []
            for row in serializer.data:
                category_list.append(
                    Category(
                        category=row["category"],
                    )
                )
            Category.objects.bulk_create(category_list)

            return Response({
                "Status": status.HTTP_200_OK,
                "Message": "Successfully upload the data",
                "Data": data
            }
            )
        else:
            category_err = serializer.errors
            return Response({
                "Status": status.HTTP_406_NOT_ACCEPTABLE,
                "Message": serializer.errors,
                "Data": category_err
            }
            )

    @action(detail=False, methods=["put"])
    def update_category(self, request, category_id):
        """
            Function to update category
        """
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        with transaction.atomic():
            categories = CategoryService.get_queryset().filter(id=category_id)
            for data in categories:
                category = CategoryService.update(data, **validated_data)
                data = {
                    "id": category.pk,
                    "Category Name": category.category,
                }
        return Response(data)

    def category_delete(self, request, category_id):
        """
         Function is used to delete category
        """
        logger.info(f"requested data is{request.data}")
        asset_queryset = AssetService.get_queryset.filter(category=category_id)
        if asset_queryset:
            message = f"Asset is connected to this Category {category_id}"
            Status = status.HTTP_405_METHOD_NOT_ALLOWED
        else:
            queryset = Category.objects.get(id=category_id)
            if queryset:
                queryset.end_date = datetime.now()
                queryset.save()
                message = f"Record deleted for id {category_id}"
                Status = status.HTTP_200_OK
            else:
                message = f"Record not found for id {category_id}"
                Status = status.HTTP_404_NOT_FOUND
        return Response(
            {
                "Status": Status,
                "Message": message
            })

    def category_details(self, request):
        """
         Function used to get details of category
        """
        logger.info(f"requested data is{request.data}")
        queryset = CategoryService.get_queryset().filter(end_date__isnull=True)
        queryset_details = []
        for data in queryset:
            query_data = ({
                "Id": data.id,
                "Category": data.category
            })
            queryset_details.append(query_data)

        return Response(
            {
                "Status": status.HTTP_200_OK,
                "Data": queryset_details
            }
        )

    def single_category_details(self, request, category_id):
        """
         Function used to get details of single category.
        """
        logger.info(f"request data is {request.data}")
        queryset = CategoryService.get_queryset().filter(id=category_id)
        if queryset:
            queryset_details = []
            for data in queryset:
                query_data = ({
                    "Id": data.id,
                    "Category": data.category
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
