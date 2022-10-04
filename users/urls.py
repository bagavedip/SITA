from django.urls import path
from rest_framework import routers

from users.views import UserViewSet

simple_router = routers.SimpleRouter()
login = UserViewSet.as_view({"post": "login"})
add_user = UserViewSet.as_view({"post": "add_user"})

urlpatterns = simple_router.urls
urlpatterns = urlpatterns + [
    path(r"api/v1/login/", login, name="login"),
    path(r"api/v1/add_user/", add_user, name="add_user")
]
