from django.db import models
from django.utils.translation import gettext_lazy as _


class Audit_ITSM(models.Model):
    """
        Model to hold data of Asset
    """
    start_date = models.DateField(_("start_date"), null=False, help_text=_("Start Date"))
    end_date = models.DateField(_("end_date"), null=True, help_text=_("End Date"))
    status = models.CharField(_("status"), null=False, help_text=_("status"))
