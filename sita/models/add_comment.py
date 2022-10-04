from django.db import models
from django.utils.translation import gettext as _


class AddComment(models.Model):
    """
     Model for Add comment
    """
    incident_id = models.CharField(_("incident_id"), max_length=200, help_text="incident_id")
    comment = models.CharField(_("comment"), max_length=200, help_text=_("comment"))
    created = models.DateField(_("created"), null=True, auto_now_add=True, help_text=_("created"))