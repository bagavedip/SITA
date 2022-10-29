from django.db import models
from django.utils.translation import gettext as _
from datetime import datetime


class STG_SIEM(models.Model):
    """
    Model to hold data for SIEM data
    """
    offense_source = models.CharField(_("offense_source"), max_length=10000, null=True, 
                                        help_text=_("Offense Source"))
    description = models.CharField(_("description"), max_length=100000, null=True, 
                                        help_text=_("Description"))
    destination_networks = models.CharField(_("destination_networks"), max_length=10000, null=True,
                                    help_text=_("Destination Network"))
    rule_name = models.CharField(_("rule_name"), max_length=10000, null=True, 
                                    help_text=_("Rule Name"))
    seim_id = models.IntegerField(_("seim_id"),
                                    help_text="SIEM Id")
    last_updated_datetime = models.DateTimeField(_("last_updated_datetime"), max_length=10000, null=True,
                                    help_text=_("Last Updated Date Time"))
    start_datetime = models.DateTimeField(_("start_datetime"), max_length=10000, null=True,
                                    help_text=_("Start Date Time"))
    policy_category_count = models.IntegerField(_("policy_category_count"), null=True,
                                    help_text=_("Policy category Count"))
    category_count = models.IntegerField(_("category_count"), null=True, 
                                    help_text=_("Category Count"))
    inactive = models.BooleanField(_("inactive"), null=True, 
                                    help_text=_("Inactive"))
    flow_count = models.IntegerField(_("flow_count"), null=True, 
                                    help_text=_("Flow Count"))
    follow_up = models.BooleanField(_("follow_up"), null=True, 
                                    help_text=_("Follow Up"))
    close_time = models.DateTimeField(_("close_time"), max_length=10000, null=True, 
                                    help_text=_("Close Time"))
    severity = models.IntegerField(_("severity"), null=True, 
                                    help_text=_("Severity"))
    credibility = models.IntegerField(_("credibility"), null=True, 
                                    help_text=_("Credibility"))
    closing_reason_id = models.IntegerField(_("closing_reason_id"), null=True, 
                                    help_text=_("Closing Reason id"))
    device_count = models.IntegerField(_("device_count"), null=True, 
                                    help_text=_("Device Count"))
    domain_id = models.IntegerField(_("domain_id"), null=True, 
                                    help_text=_("Domain Id"))
    username_count = models.IntegerField(_("username_count"), null=True, 
                                    help_text=_("Username Count"))
    protected = models.BooleanField(_("protected"), null=True, 
                                    help_text=_("Protected"))
    relevance = models.IntegerField(_("relevance"), null=True, 
                                    help_text=_("Relevance"))
    source_network = models.CharField(_("source_network"), max_length=10000, null=True, 
                                    help_text=_("Source Network"))
    status = models.CharField(_("status"), max_length=10000, null=True, 
                                    help_text=_("Status"))
    source_count = models.IntegerField(_("source_count"), null=True, 
                                    help_text=_("Source Count"))
    rules = models.CharField(_("rules"), max_length=10000, null=True, 
                                    help_text=_("Rules"))
    assigned_to = models.CharField(_("assigned_to"), max_length=10000, null=True,
                                    help_text=_("Assigned To"))
    offense_type = models.IntegerField(_("offense_type"), null=True, 
                                    help_text=_("Offense Type"))
    security_category_count = models.IntegerField(_("security_category_count"), null=True,
                                    help_text=_("Security Category Count"))
    remote_destination_count = models.IntegerField(_("remote_destination_count"), null=True,
                                    help_text=_("Remote Destination Count"))
    categories = models.CharField(_("categories"), max_length=10000, null=True, 
                                    help_text=_("Categories"))
    event_count = models.IntegerField(_("event_count"), null=True, 
                                    help_text=_("Event Count"))
    local_destination_count = models.IntegerField(_("local_destination_count"), null=True,
                                    help_text=_("Local Destination Count"))
    log_sources = models.CharField(_("log_sources"), max_length=10000, null=True, 
                                    help_text=_("Log Sources"))
    magnitude = models.IntegerField(_("magnitude"), null=True, 
                                    help_text=_("Magnitude"))
    closing_user = models.CharField(max_length=10000,null= True, 
                                    help_text="Closing User")
    source_address_ids = models.CharField(_("source_address_ids"), max_length=10000, null=True,
                                    help_text=_("Source address ids"))
    local_destination_address_ids = models.CharField(_("local_destination_address_ids"), max_length=10000, null=True,
                                    help_text=_("Local destination address ids"))
    first_persisted_time = models.DateTimeField(_("first_persisted_time"), max_length=10000,null=True, 
                                    help_text="first_persisted_time")
    last_persisted_time = models.DateTimeField(_("last_persisted_time"), max_length=10000,null=True, 
                                    help_text="last_persisted_time")
    rule_details = models.CharField(max_length=10000, null=True, 
                                    help_text="rule_details")
    created_at = models.DateTimeField(_("created at"), default=datetime.now, help_text=_("created at"))
    asset = models.CharField(max_length=200, null=True, help_text="Asset_name")
    asset_type = models.CharField(max_length=200, null=True, help_text="Asset_type")
    asset_id = models.CharField(max_length=200, null=True, help_text="Asset_id")
    asset_type_id = models.CharField(max_length=200, null=True, help_text="Asset_type_id")



