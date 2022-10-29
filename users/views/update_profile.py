import logging

from django.core.files.base import ContentFile
from django.utils import timezone
from django.db import transaction, IntegrityError
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated

from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from users.models import User
from users.serializers.user import UserUpdateSerializer, AddUserSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from users.services.user import UserService

logger = logging.getLogger(__name__)

class UserUpdate(mixins.CreateModelMixin, viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated]

    def update_name(self, request):
        request_user = request.data
        request_data = {
            "email":request_user["email"],
            "first_name":request_user["firstName"],
            "last_name":request_user["lastName"],
            "phone_code": request_user["phone_code"],
            "phone_number": request_user["phone_number"],
            "profile_photo": request_user["profile_photo"],
            "profile_photo_name": request_user["profile_photo_name"]
        }
        serializer = UserUpdateSerializer(data = request_data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        if serializer.is_valid():
            updated_user = User.objects.get(email = request_user.get("email"))
            if request_user.get("firstName"):
                updated_user.first_name = validated_data["first_name"]
            if request_user.get("lastName"):
                updated_user.last_name = validated_data["last_name"]
            if request_user.get("phone_number"):
                updated_user.phone_number = validated_data["phone_number"]
            if request_user.get("phone_code"):
                updated_user.phone_code = validated_data["phone_code"]
            updated_user.profile_photo = None if request_user.get("profile_photo") is None else ContentFile(
                request_user.get("profile_photo"), name=request_user.get("profile_photo_name"))

            updated_user.save()
            return Response(
                {
                "Data":serializer.data, 
                "status": "SUCCESS",
                "message": "User Updated Successfully!!"
                }
            )
        else:
            return Response(
                {
                "Data":serializer.data, 
                "status": "SUCCESS",
                "message": "Oops!! Something went wrong"
                }
            )
