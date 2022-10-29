from django.urls import path
from rest_framework import routers

from users.views.preference import PreferenceViewSet
from users.views.users import UserViewSet
from users.views.update_profile import UserUpdate
from users.views.update_password import PasswordUpdate
from users.views.sent_mail import UserSentMail
from users.views.forget_password import PasswordReset

simple_router = routers.SimpleRouter()
login = UserViewSet.as_view({"post": "login"})
add_user = UserViewSet.as_view({"post": "add_user"})
update_user = UserUpdate.as_view({"post": "update_name"})
update_user_password = PasswordUpdate.as_view({"post": "update_password"})
sent_mail = UserSentMail.as_view({"post": "sent_mail"})
session_check = UserSentMail.as_view({"post": "decrypt_hashcode"})
reset_password = PasswordReset.as_view({"post":"reset_password"})

preference_input = PreferenceViewSet.as_view({"post": "preference_input"})
preference_fetch = PreferenceViewSet.as_view({"post": "preference_fetch"})

urlpatterns = simple_router.urls
urlpatterns = urlpatterns + [
    path(r"api/v1/login/", login, name="login"),
    path(r"api/v1/add_user/", add_user, name="add_user"),
    path(r"api/v1/update_user/", update_user, name="update_user"),
    path(r"api/v1/update_password/", update_user_password, name="update_user_password"),
    path(r"api/v1/forget_password/", sent_mail, name="forget_password"),
    path(r"api/v1/reset_password/", reset_password, name="reset_password"),
    path(r"api/v1/session_check/", session_check, name="session_check"),
    path(r"api/v1/preference_input/", preference_input, name="preference_input"),
    path(r"api/v1/preference_fetch/", preference_fetch, name="preference_fetch"),
]
