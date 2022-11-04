from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models.role import Role

from users.managers import CustomUserManager


class User(AbstractUser):
    username = None
    id = models.BigAutoField(_("id"),primary_key=True)
    email = models.EmailField(_("email"),help_text="User email",unique=True,max_length=255)
    first_name = models.CharField(_("first_name"),max_length=50,help_text="first name")
    last_name = models.CharField(_("last_name"),max_length=50,help_text="last_name")
    is_admin = models.BooleanField(_("is_admin"),help_text="is_admin")
    key = models.BinaryField(_("key"), null=True)
    role_id = models.ForeignKey(Role,null=True,on_delete=models.CASCADE,
                                help_text=_("Role Name"))
    phone_number = models.CharField(_("phone number"),max_length=20,null=True)
    profile_photo = models.FileField(_("profile_photo"),upload_to='profile_photos',help_text="profile_photo",default="", null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['is_admin', 'first_name', 'last_name']  # Email & Password are required by default.

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self,*args,**kwargs):
        self.username = self.email
        return super().save(*args,**kwargs)