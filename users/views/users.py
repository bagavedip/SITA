import logging

from django.db import transaction, IntegrityError
from django.utils import timezone
from django.contrib.auth.hashers import make_password

from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import Preference
from users.serializers.user import LoginSerializer, UserSerializer, AddUserSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from users.services.user import UserService

logger = logging.getLogger(__name__)


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    View for handling User's login and adding user
    """
    service_class = UserService
    serializer_class = LoginSerializer

    def get_service(self):
        """
        Function which return user service
        """
        return self.service_class()

    def get_auth_tokens(self, user):
        """
        Function to create access and refresh token for a user
        """
        login_time_data = {"last_login": timezone.now()}
        user = UserService.update(user, login_time_data)
        token = RefreshToken.for_user(user)
        return {
            "access_token": str(token.access_token),
            "refresh_token": str(token),
        }

    def email_login(self, payload):
        """
        function for Email login
        """
        logger.info("Log in via email and password.")
        user = self.get_service().get_active_user_by_email(payload["email"])
        # check user is exists
        if user is None:
            logger.error(f"No user found with the email: {payload['email']}")
            raise AuthenticationFailed

        # check password
        if not user.check_password(payload["password"]):
            logger.error("Password verification failed.")
            raise AuthenticationFailed
        if not Preference.objects.filter(user=user):
            Preference.objects.create(user=user, session={"oei": {"day_filter": "1 Day"},
                                                          "insights": {"day_filter": "1 Day"},
                                                          "perspective": {"day_filter": "1 Day"}})
        else:
            pass
        data = self.get_auth_tokens(user)
        data.update({"user": UserSerializer(user).data})
        data["user"]["profile_photo"] = None if bool(user.profile_photo) is False \
            else user.profile_photo.read()
        data["user"]["profile_photo_name"] = None if bool(user.profile_photo) is False \
            else str(user.profile_photo).split('/')[1]

        return data

    @action(detail=False, methods=["post"])
    def login(self, request, **kwargs):
        """
         Function for login user
        """
        logger.info("Validating data for Log In.")
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        logger.info("Initiating Log in.")

        # Parse action and payload from request
        login_action = validated_data["action"]
        login_payload = validated_data["payload"]

        if login_action == serializer.EMAIL_LOGIN:
            response_data = self.email_login(login_payload)
        logger.info("Log in Successful.")
        return Response(response_data)

    def add_user(self, request):
        """
         Function for add user at admin side
        """
        serializer = AddUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        with transaction.atomic():
            password = make_password(validated_data["password"])
            try:
                if serializer.is_valid():
                    serializer.save(password=password)
                    return Response(
                        {
                            "Data": serializer.data,
                            "Status": status.HTTP_201_CREATED,
                            "Message": "User Added Successfully!!"
                        }
                    )
            except IntegrityError:
                return Response({
                    "Data": serializer.data,
                    "Status": status.HTTP_208_ALREADY_REPORTED,
                    "Message": "Email Already Added!!"
                })
