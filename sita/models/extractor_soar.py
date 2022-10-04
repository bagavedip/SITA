from django.db import models
from django.utils.translation import gettext as _


class EXTRACTOR_SOAR(models.Model):
    """
    Model to hold data for SOAR data
    """
    SOAR_ID = models.CharField(_("SOAR_ID"), max_length=2000, null=True, help_text=_("SOAR Id"))
    AssignedUser = models.CharField(_("AssignedUser"), max_length=2000, null=True, help_text=_("Assigned User"))
    Title = models.CharField(_("Title"), max_length=2000, null=True, help_text=_("Title"))
    Time = models.CharField(_("Time"), max_length=2000, null=True, help_text=_("Time"))
    Tags = models.CharField(_("Tags"), max_length=2000, null=True, help_text=_("Tags"))
    Products = models.CharField(_("Products"), max_length=2000, null=True, help_text=_("Product"))
    Incident = models.CharField(_("Incident"), max_length=2000, null=True, help_text=_("Incident"))
    Suspicious = models.CharField(_("Suspicious"), max_length=2000, null=True, help_text=_("Suspicious"))
    Important = models.CharField(_("Important"), max_length=2000, null=True, help_text=_("Important"))
    Ports = models.CharField(_("Ports"), max_length=2000, null=True, help_text=_("Ports"))
    Outcomes = models.CharField(_("Outcomes"), max_length=2000, null=True, help_text=_("Outcomes"))
    Status = models.CharField(_("Status"), max_length=2000, null=True, help_text=_("Status"))
    Environment = models.CharField(_("Environment"), max_length=2000, null=True, help_text=_("Environment"))
    Priority = models.CharField(_("Priority"), max_length=2000, null=True, help_text=_("Priority"))
    Stage = models.CharField(_("Stage"), max_length=2000, null=True, help_text=_("Stage"))
    TicketIDs = models.CharField(_("TicketIDs"), max_length=2000, help_text=_("Ticket Ids"))
    ClosingTime = models.CharField(_("ClosingTime"), max_length=2000, null=True, help_text=_("Closing Time"))
    Sources = models.CharField(_("Sources"), max_length=2000, null=True, help_text=_("Sources"))
    Reason = models.CharField(_("Reason"), max_length=2000, null=True, help_text=_("Reason"))
    RootCause = models.CharField(_("RootCause"), max_length=2000, null=True, help_text=_("Root Cause"))
    Case_id = models.CharField(_("Case_id"), null=True, max_length=2000, help_text=_("Case Id"))
    AlertsCount = models.CharField(null=True, max_length=2000, help_text="alertscount")
