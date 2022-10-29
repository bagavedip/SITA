from django.db import models
from django.utils.translation import gettext_lazy as _

from sita.models.security_pulse import SecurityPulse


class SecurityPulseImage(models.Model):
    id = models.BigAutoField(_("security_pulse_id"), primary_key=True)
    security_pulse = models.ForeignKey(SecurityPulse, on_delete=models.CASCADE, null=True, db_index=False,
                                       verbose_name=_("security_pulse"), help_text=_("security_pulse"),
                                       related_name="+")
    image_data = models.FileField(_("image_data"), upload_to="perspective/donut_graph", null=True,
                                  help_text=_("image_data"))
    info = models.TextField(_("info"), null=True, help_text=_("info"))
