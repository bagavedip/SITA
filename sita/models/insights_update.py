from django.db import models
from django.utils.translation import gettext as _

class HubUpdate(models.Model):

    soar_id = models.CharField(_("soar_id"), max_length=100, help_text=_("soar_id"))
    updates = models.CharField(_("updates"), max_length=200, help_text=_("updates"))
    update_date = models.DateTimeField(_("update_date"), auto_now_add=True, help_text=_("update_date"))
    updated_by = models.CharField(_("updated_by"), max_length=100, help_text=_("updated_by"))
    
