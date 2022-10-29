from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    id = models.BigAutoField(_("id"), primary_key=True)
    name = models.CharField(_('role'), max_length = 100, help_text = "Role", null = True)


    def __str__(self):
        return self.id
