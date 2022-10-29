from django.db import models
from django.utils.translation import gettext as _
from colorfield.fields import ColorField


class FACT_INSIGHTS(models.Model):
    """
    Model to hold Hub data of insights
    """

    class Criticality(models.TextChoices):
        HIGH = "HIGH", _("High"),
        MEDIUM = "MEDIUM", _("Medium"),
        LOW = "LOW", _("Low")
    entity_id = models.CharField(_("entity_id"), max_length=2000, help_text=_("entity id"), null=True)
    entity_name = models.CharField(_("entity_name"), max_length=2000, null=True, help_text=_("entity name"))
    entity_color = ColorField(_("entity_color"), format='hexa', null=True, help_text=_("entity color"))
    location_id = models.CharField(_("location_id"), max_length=2000, help_text=_("location id"), null=True)
    location_name = models.CharField(_("location_name"), null=True, max_length=2000, help_text=_("location name"))
    function_id = models.CharField(_("function_id"), max_length=2000, help_text=_("function id"), null=True)
    function_name = models.CharField(_("function_name"), max_length=2000, null=True, help_text=_("function name"))
    asset_id = models.CharField(_("asset_id"), max_length=2000, help_text=_("asset id"), null=True)
    asset_name = models.CharField(_("asset_name"), max_length=2000, null=True, help_text=_("asset name"))
    asset_type = models.CharField(_("asset_type"), max_length=2000, null=True, help_text=_("asset type"))
    asset_color = ColorField(_("asset_color"), format='hexa', null=True, help_text=_("asset color"))
    usecase_id = models.CharField(_("usecase_id"), max_length=2000, help_text=_("use_case id"), null=True)
    use_case = models.CharField(_("use_case"), max_length=2000, null=True, help_text=_("use case"))
    rule_id = models.CharField(_("rule_id"), max_length=2000, help_text=_("rule id"), null=True)
    rule_name = models.CharField(_("rule_name"), max_length=2000, null=True, help_text=_("rule name"))
    seim_id = models.CharField(_("seim_id"), max_length=2000, help_text=_("seim id"), null=True)
    severity = models.IntegerField(_("severity"), null=True, help_text=_("Severity"))
    events = models.IntegerField(_("events"), null=True, help_text=_("events"))
    starttime = models.DateTimeField(_("event start time"), null=True, help_text=_("event start time"))
    endtime = models.DateTimeField(_("event end date"), null=True, help_text=_("event end time"))
    magnitude = models.IntegerField(_("magnitude"), null=True, help_text=_("Magnitude"))
    criticality = models.CharField(_("criticality"), max_length=256, null=True, choices=Criticality.choices,
                                   help_text=_("criticality"))
    criticality_color = ColorField(_("criticality_color"), null=True, help_text=_("criticality color"))
    description = models.CharField(_("description"), max_length=20000, help_text=_("description"), null=True)
    itsm_id = models.CharField(_("itsm_id"), max_length=2000, help_text=_("itsm id"), null=True)
    status = models.CharField(_("request_status"), max_length=2000, help_text=_("request status"), null=True)
    priority = models.CharField(_("priority"), max_length=2000, help_text=_("priority"), null=True)
    group = models.CharField(_("group"), max_length=2000, help_text=_("group"), null=True)
    service_category = models.CharField(_("category"), max_length=2000, help_text=_("category"), null=True)
    assigned_time = models.DateTimeField(_("assigned_time"), max_length=2000, null=True, help_text=_("Time send mail"))
    resolution = models.CharField(_("resolution"), max_length=10000, help_text=_("resolution"), null=True)
    assets = models.CharField(_("assets"), max_length=2000, help_text=_("log source"), null=True)
    site = models.CharField(_("site"), max_length=2000, help_text=_("location"), null=True)
    replys = models.CharField(_("replys"), max_length=2000, help_text=_("Replies"), null=True)
    created_time = models.CharField(_("created_time"), max_length=2000, help_text=_("created time"), null=True)
    is_overdue = models.CharField(_("is_overdue"), max_length=2000, help_text=_("Overdue Status"), null=True)
    due_by_time = models.CharField(_("due_by_time"), max_length=2000, help_text=_("DueBy Time"), null=True)
    first_response_due_by_time = models.CharField(_("first_response_due_by_time"), max_length=2000,
                                                  help_text=_("First Response overdue status"), null=True)
    is_first_response_overdue = models.CharField(_("is_first_response_overdue"), max_length=2000, null=True,
                                                 help_text=_("Response DueBy Time"))
    impact = models.CharField(_("impact"), max_length=2000, help_text=_("impact"), null=True)
    urgency = models.CharField(_("urgency"), max_length=2000, help_text=_("urgency"), null=True)
    soar_id = models.CharField(_("soar_id"), max_length=20000, help_text=_("soar id"), null=True)
    ticket_id = models.CharField(_("ticket_id"), max_length=2000, help_text=_("ticket id"), null=True)
    Suspicious = models.CharField(_("Suspicious"), max_length=2000, help_text=_("suspicious"), null=True)
    subject = models.CharField(_("subject"), max_length=2000, help_text=_("subject"), null=True)
    last_updated_datetime = models.DateTimeField(_("last_updated_time"), null=True, max_length=2000,
                                                 help_text=_("last_updated_time"))
    target = models.CharField(_("target_ip"), max_length=2000, help_text=_("target"), null=True)
