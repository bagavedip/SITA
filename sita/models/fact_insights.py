from django.db import models
from django.utils.translation import gettext as _
from colorfield.fields import ColorField


class FACT_INSIGHTS(models.Model):
    """
    Model to hold Hub data of insights
    """

    entity_id = models.CharField(_("entity_id"),null=True,max_length=10000,
                               help_text=_("entity_id"))
    entity_name = models.CharField(_("entity_name"),null=True,max_length=10000,
                               help_text=_("entity_name"))
    entity_color = models.CharField(_("entity_color"),null=True,max_length=10000,
                               help_text=_("entity_color"))
    location_id = models.CharField(_("location_id"),null=True,max_length=10000,
                               help_text=_("location_id"))
    location_name = models.CharField(_("location_name"),null=True,max_length=10000,
                               help_text=_("location_name"))
    function_id = models.CharField(_("function_id"),null=True,max_length=10000,
                               help_text=_("function_id"))
    function_name = models.CharField(_("function_name"),null=True,max_length=10000,
                               help_text=_("function_name"))
    asset_id = models.CharField(_("asset_id"),null=True,max_length=10000,
                               help_text=_("asset_id"))
    asset_name = models.CharField(_("asset_name"),null=True,max_length=10000,
                               help_text=_("asset_name"))
    asset_type = models.CharField(_("asset_type"),null=True,max_length=10000,
                               help_text=_("asset_type"))
    asset_color = models.CharField(_("asset_color"),null=True,max_length=10000,
                               help_text=_("asset_color"))
    usecase_id = models.CharField(_("usecase_id"),null=True,max_length=10000,
                               help_text=_("usecase_id"))
    use_case = models.CharField(_("use_case"),null=True,max_length=10000,
                               help_text=_("use_case"))
    rule_id = models.CharField(_("rule_id"),null=True,max_length=10000,
                               help_text=_("rule_id"))
    rule_name = models.CharField(_("rule_name"),null=True,max_length=10000,
                               help_text=_("rule_name"))
    seim_id = models.CharField(_("seim_id"),null=True,max_length=10000,
                               help_text=_("seim_id"))
    events = models.CharField(_("events"),null=True,max_length=10000,
                               help_text=_("events"))
    starttime = models.DateTimeField(_("starttime"),null=True,max_length=10000,
                               help_text=_("starttime"))
    endtime = models.DateTimeField(_("endtime"),null=True,max_length=10000,
                               help_text=_("endtime"))
    description = models.CharField(_("description"),null=True,max_length=10000,
                               help_text=_("description"))
    itsm_id = models.CharField(_("itsm_id"),null=True,max_length=10000,
                               help_text=_("itsm_id"))
    status = models.CharField(_("status"),null=True,max_length=10000,
                               help_text=_("status"))
    priority = models.CharField(_("priority"),null=True,max_length=10000,
                               help_text=_("priority"))
    group = models.CharField(_("group"),null=True,max_length=10000,
                               help_text=_("group"))
    service_category = models.CharField(_("service_category"),null=True,max_length=10000,
                               help_text=_("service_category"))
    assigned_time = models.CharField(_("assigned_time"),null=True,max_length=10000,
                               help_text=_("assigned_time"))
    resolution = models.CharField(_("resolution"),null=True,max_length=10000,
                               help_text=_("resolution"))
    assets = models.CharField(_("assets"),null=True,max_length=10000,
                               help_text=_("assets"))
    site = models.CharField(_("site"),null=True,max_length=10000,
                               help_text=_("site"))
    replys = models.CharField(_("replys"),null=True,max_length=10000,
                               help_text=_("replys"))
    created_time = models.CharField(_("created_time"),null=True,max_length=10000,
                               help_text=_("Id"))
    is_overdue = models.CharField(_("is_overdue"),null=True,max_length=10000,
                               help_text=_("Id"))
    due_by_time = models.CharField(_("due_by_time"),null=True,max_length=10000,
                               help_text=_("Id"))
    first_response_due_by_time = models.CharField(_("first_response_due_by_time"),null=True,max_length=10000,
                               help_text=_("first_response_due_by_time"))
    is_first_response_overdue = models.CharField(_("is_first_response_overdue"),null=True,max_length=10000,
                               help_text=_("is_first_response_overdue"))
    impact = models.CharField(_("impact"),null=True,max_length=10000,
                               help_text=_("impact"))
    urgency = models.CharField(_("urgency"),null=True,max_length=10000,
                               help_text=_("urgency"))
    subject = models.CharField(_("subject"),null=True,max_length=10000,
                               help_text=_("subject"))
    comments = models.CharField(_("comments"),null=True,max_length=10000,
                               help_text=_("comments"))
    soar_id = models.CharField(_("soar_id"),null=True,max_length=10000,
                               help_text=_("soar_id"))
    ticket_id = models.CharField(_("ticket_id"),null=True,max_length=10000,
                               help_text=_("ticket_id"))
    Suspicious = models.CharField(_("Suspicious"),null=True,max_length=10000,
                               help_text=_("Suspicious"))

