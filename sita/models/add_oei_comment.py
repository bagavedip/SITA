from django.db import models
from django.utils.translation import gettext as _


class AddOeiComment(models.Model):

    ticket_id = models.CharField(_("ticket_id"), max_length=200, help_text="ticket_id")
    comment = models.CharField(_("comment"), max_length=200, help_text=_("comment"))
    created = models.DateField(_("created"), null=True, auto_now_add=True, help_text=_("created"))
