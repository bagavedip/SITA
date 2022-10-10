from django.db import models
from django.utils.translation import gettext as _


class EXTRACTOR_SIEM(models.Model):
    """
    Model to hold data for SIEM data
    """

    last_persisted_time = models.CharField(_("last_persisted_time"),  max_length=10000, null=True, 
                                               help_text=_("last_persisted_time"))
    username_count = models.CharField(_("username_count"), max_length=10000, null=True, 
                                      help_text=_("username_count"))
    description = models.CharField(_("description"), max_length=10000, null=True, 
                                   help_text=_("description"))
    rules = models.CharField(_("rules"), max_length=10000, null=True, 
                             help_text=_("rules"))
    event_count = models.CharField(_("event_count"), max_length=10000, null=True, 
                                   help_text=_("event_count"))
    flow_count = models.CharField(_("flow_count"), max_length=10000, null=True, 
                                  help_text=_("flow_count"))
    assigned_to = models.CharField(_("assigned_to"), max_length=10000, null=True, 
                                   help_text=_("assigned_to"))
    security_category_count = models.CharField(_("security_category_count"), max_length=10000, null=True, 
                                               help_text=_("security_category_count"))
    follow_up = models.CharField(_("follow_up"), max_length=10000, null=True, 
                                 help_text=_("follow_up"))
    source_address_ids = models.CharField(_("source_address_ids"), max_length=10000, null=True, 
                                          help_text=_("source_address_ids"))
    source_count = models.CharField(_("source_count"), max_length=10000, null=True, 
                                    help_text=_("source_count"))
    inactive = models.CharField(_("inactive"), max_length=10000, null=True, 
                                help_text=_("inactive"))
    protected = models.CharField(_("protected"), max_length=10000, null=True, 
                                 help_text=_("protected"))
    closing_user = models.CharField(_("closing_user"), max_length=10000, null=True, 
                                    help_text=_("closing_user"))
    destination_networks = models.CharField(_("destination_networks"), max_length=10000, null=True, 
                                            help_text=_("destination_networks"))
    source_network = models.CharField(_("source_network"), max_length=10000, null=True, 
                                      help_text=_("source_network"))
    category_count = models.CharField(_("category_count"), max_length=10000, null=True, 
                                      help_text=_("category_count"))
    close_time = models.CharField(_("close_time"), max_length=10000, null=True, 
                                      help_text=_("close_time"))
    remote_destination_count = models.CharField(_("remote_destination_count"), max_length=10000, null=True, 
                                                help_text=_("remote_destination_count"))
    start_time = models.CharField(_("start_time"), max_length=10000, null=True, 
                                      help_text=_("start_time"))
    magnitude = models.CharField(_("magnitude"), max_length=10000, null=True, 
                                 help_text=_("magnitude"))
    last_updated_time = models.CharField(_("last_updated_time"), max_length=10000, null=True, 
                                             help_text=_("last_updated_time"))
    credibility = models.CharField(_("credibility"), max_length=10000, null=True, 
                                   help_text=_("credibility"))
    siem_id = models.CharField(_("id"), max_length=10000, null=True, 
                               help_text=_("id"))
    categories = models.CharField(_("categories"), max_length=10000, null=True, 
                                  help_text=_("categories"))
    severity = models.CharField(_("severity"), max_length=10000, null=True, 
                                help_text=_("severity"))
    policy_category_count = models.CharField(_("policy_category_count"), max_length=10000, null=True, 
                                             help_text=_("policy_category_count"))
    log_sources = models.JSONField(_("log_sources"), max_length=10000, null=True, 
                                   help_text=_("log_sources"))
    closing_reason_id = models.CharField(_("closing_reason_id"), max_length=10000, null=True, 
                                         help_text=_("closing_reason_id"))
    device_count = models.CharField(_("device_count"), max_length=10000, null=True, 
                                    help_text=_("device_count"))
    first_persisted_time = models.CharField(_("first_persisted_time"), max_length=10000, null=True, 
                                                help_text=_("first_persisted_time"))
    offense_type = models.CharField(_("offense_type"), max_length=10000, null=True, 
                                    help_text=_("offense_type"))
    relevance = models.CharField(_("relevance"), max_length=10000, null=True, 
                                 help_text=_("relevance"))
    domain_id = models.CharField(_("domain_id"), max_length=10000, null=True, 
                                 help_text=_("domain_id"))
    offense_source = models.CharField(_("offense_source"), max_length=10000, null=True, 
                                      help_text=_("offense_source"))
    local_destination_address_ids = models.CharField(_("local_destination_address_ids"), max_length=10000, null=True, 
                                                     help_text=_("local_destination_address_ids"))
    local_destination_count = models.CharField(_("local_destination_count"), max_length=10000, null=True, 
                                               help_text=_("local_destination_count"))
    status = models.CharField(_("status"), max_length=10000, null=True, 
                              help_text=_("status"))
    rule_details = models.CharField(_("rule_details"), max_length=10000, null=True, 
                                    help_text=_("rule_details"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, help_text=_("created at"))
