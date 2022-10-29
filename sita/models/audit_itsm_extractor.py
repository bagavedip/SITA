from django.db import models
from django.utils.translation import gettext_lazy as _


class Audit_ITSM(models.Model):
    """
        Model to hold data of Asset
    """
    start_date = models.DateTimeField(_("start_date"), null=True, help_text=_("Start Date"))
    end_date = models.DateTimeField(_("end_date"), null=True, help_text=_("End Date"))
    status = models.CharField(_("status"), null=False, help_text=_("status"), max_length = 200)
    no_dump_data = models.IntegerField(_("no_dump_data"),null=True,
                                   help_text=_("no_dump_data"))
    total_data = models.IntegerField(_("total_data"),null=True,
                                   help_text=_("total_data"))
