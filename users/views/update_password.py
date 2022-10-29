import logging
from django.db import transaction
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed

from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from users.models import User
from users.serializers.user import PasswordUpdateSerializer

logger = logging.getLogger(__name__)

class PasswordUpdate(mixins.CreateModelMixin, viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated]

    def update_password(self, request):
        request_user = request.data
        request_data = {
            "email":request_user["email"],
            "oldPassword":request_user["oldPassword"],
            "password":request_user["newPassword"]
            }
        serializer = PasswordUpdateSerializer(data = request_data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        with transaction.atomic():
            password = make_password(validated_data["password"])
            if serializer.is_valid():
                updated_user = User.objects.get(email = validated_data["email"])
                if not updated_user.check_password(request_user["oldPassword"]):
                    logger.error("Password verification failed.")
                    raise AuthenticationFailed
                updated_user.password  = password
                updated_user.save()
                return Response(
                    {
                    "status":"SUCCESS",
                    "message": "Password Reset Successfully!!"
                    }
                )
            else:
                return Response(
                    {
                    "Data":serializer.data, 
                    "status":"FAIL",
                    "message": "Oops! Something went wrong."
                    }
                )
