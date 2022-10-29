from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords
from datetime import datetime


class STG_ITSM(models.Model):
    """
    Model to hold data for ITSM data
    """
    itsm_id = models.CharField(_("id"),null=True,max_length=10000,
                               help_text=_("Id"))
    resolution_submitted_on_display_value = models.DateTimeField(_("resolution_submitted_on_display_value"),max_length=10000,
                                                             null=True,blank=True,
                                                             help_text=_("Resolution on display value"))
    resolution_submitted_on_value = models.CharField(_("resolution_submitted_on_value"),null=True,max_length=10000,
                                                     help_text=_("Resolution on value"))
    resolution_submitted_by_email_id = models.CharField(_("resolution_submitted_by_email_id"),null=True,max_length=10000,
                                                        help_text=_("Resolution on Email id"))
    resolution_submitted_by_name = models.CharField(_("resolution_submitted_by_name"),null=True,max_length=10000,
                                                    help_text=_("Resolution on name"))
    resolution_submitted_by_mobile = models.CharField(_("resolution_submitted_by_mobile"),null=True,max_length=10000,
                                                      help_text=_("Resolution on Mobile"))
    resolution_submitted_by_is_vipuser = models.CharField(_("resolution_submitted_by_is_vipuser"),null=True,
                                                          max_length=10000,
                                                          help_text=_("Resolution on vipuser"))
    resolution_submitted_by_id = models.CharField(_("resolution_submitted_by_id"),null=True,max_length=10000,
                                                  help_text=_("Resolution by id"))
    resolution_submitted_by_status = models.CharField(_("resolution_submitted_by_status"),null=True,max_length=10000,
                                                      help_text=_("Resolution on Status"))
    resolution_resolution_attachments = models.CharField(_("resolution_resolution_attachments"),null=True,
                                                         max_length=10000,
                                                         help_text=_("Resolution on Attachment"))
    resolution_content = models.CharField(_("resolution_content"),null=True,max_length=10000,
                                          help_text=_("Resolution Content"))
    linked_to_request = models.CharField(_("linked_to_request"),null=True,max_length=10000,
                                         help_text=_("Linked Request"))
    mode_name = models.CharField(_("mode_name"),null=True,max_length=10000,
                                 help_text=_("Mode name"))
    mode_id = models.IntegerField(_("mode_id"),null=True,
                               help_text=_("Mode id"))
    lifecycle = models.CharField(_("lifecycle"),null=True,max_length=10000,
                                 help_text=_("Lifecycle"))
    assets = models.CharField(_("assets"),null=True,max_length=10000,
                              help_text=_("Assets"))
    is_trashed = models.BooleanField(_("is_trashed"),null=True,
                                  help_text=_("Is trashed"))
    assigned_time_display_value = models.DateTimeField(_("assigned_time_display_value"),max_length=10000,null=True,blank=True,
                                                   help_text=_("Assigned time display value"))
    assigned_time_value = models.CharField(_("assigned_time_value"),null=True,max_length=10000,
                                           help_text=_("Assigned time value"))
    group_name = models.CharField(_("group_name"),null=True,max_length=10000,
                                  help_text=_("Group Name"))
    group_id = models.IntegerField(_("group_id"),null=True,
                                help_text=_("Group Id"))
    requester_email_id = models.CharField(_("requester_email_id"),null=True,max_length=10000,
                                          help_text=_("Requester Email Id"))
    requester_name = models.CharField(_("requester_name"),null=True,max_length=10000,
                                      help_text=_("Requester name"))
    requester_mobile = models.CharField(_("requester_mobile"),null=True,max_length=10000,
                                        help_text=_("Requester Mobile"))
    requester_is_vipuser = models.BooleanField(_("requester_is_vipuser"),null=True,
                                            help_text=_("Requester vipuser"))
    requester_id = models.IntegerField(_("requester_id"),null=True,
                                    help_text=_("Requester ID"))
    requester_status = models.CharField(_("requester_status"),null=True,max_length=10000,
                                        help_text=_("Requester Status"))
    email_to = models.CharField(_("email_to"),null=True,max_length=10000,
                                help_text=_("Requester ID"))
    created_time_display_value = models.DateTimeField(_("created_time_display_value"),max_length=10000,null=True,blank=True,
                                                  help_text=_("Created time display value"))
    created_time_value = models.CharField(_("created_time_value"),null=True,max_length=10000,
                                          help_text=_("Created time Value"))
    has_resolution_attachments = models.BooleanField(_("has_resolution_attachments"),null=True,
                                                  help_text=_("Resolution Attachments"))
    approval_status = models.CharField(_("approval_status"),null=True,max_length=10000,
                                       help_text=_("Approva Status"))
    impact_name = models.CharField(_("impact_name"),max_length=10000,null=True,
                                   help_text=_("Impact Name"))
    impact_id = models.IntegerField(_("impact_id"),null=True,
                                 help_text=_("Impact Id"))
    service_category_name = models.CharField(_("service_category_name"),null=True,max_length=10000,
                                             help_text=_("Service Category Name"))
    service_category_id = models.IntegerField(_("service_category_id"),null=True,
                                           help_text=_("Service Category Id"))
    sla_name = models.CharField(_("sla_name"),max_length=10000,null=True,
                                help_text=_("SLA Name"))
    sla_id = models.IntegerField(_("sla_id"),null=True,
                              help_text=_("SLA Id"))
    resolved_time_display_value = models.DateTimeField(_("resolved_time_display_value"),max_length=10000,null=True,blank=True,
                                                   help_text=_("Resolved time display value"))
    resolved_time_value = models.CharField(_("resolved_time_value"),max_length=10000,null=True,
                                           help_text=_("Resolved time value"))
    priority_color = models.CharField(_("priority_color"),null=True,max_length=10000,
                                      help_text=_("Priority color"))
    priority_name = models.CharField(_("priority_name"),max_length=10000,null=True,
                                     help_text=_("Priority Name"))
    priority_id = models.IntegerField(_("priority_id"),null=True,
                                   help_text=_("Priority Id"))
    created_by_email_id = models.CharField(_("created_by_email_id"),null=True,max_length=10000,
                                           help_text=_("Created By Email Id"))
    created_by_name = models.CharField(_("created_by_name"),max_length=10000,null=True,
                                       help_text=_("Created By Name"))
    created_by_mobile = models.CharField(_("created_by_mobile"),max_length=10000,null=True,
                                         help_text=_("Created by Mobile"))
    created_by_is_vipuser = models.BooleanField(_("created_by_is_vipuser"),null=True,
                                             help_text=_("Created By is vipuser"))
    created_by_id = models.IntegerField(_("created_by_id"),null=True,
                                     help_text=_("Created By id"))
    created_by_status = models.CharField(_("created_by_status"),max_length=10000,null=True,
                                         help_text=_("Created by status"))
    first_response_due_by_time_display_value = models.DateTimeField(_("first_response_due_by_time_display_value"),null=True,
                                                                max_length=10000,blank=True,
                                                                help_text=_("First response due by time"))
    first_response_due_by_time_value = models.CharField(_("first_response_due_by_time_value"),max_length=10000,null=True,
                                                        help_text=_("First response due by time value"))
    last_updated_time_display_value = models.DateTimeField(_("last_updated_time_display_value"),max_length=10000,null=True,blank=True,
                                                       help_text=_("Last updated time"))
    last_updated_time_value = models.CharField(_("last_updated_time_value"),null=True,max_length=10000,
                                               help_text=_("Last updated time value"))
    has_notes = models.BooleanField(_("has_notes"),null=True,
                                 help_text=_("Has notes"))
    udf_fields_udf_sline_4501 = models.CharField(_("udf_fields_udf_sline_4501"),max_length=10000,null=True,
                                                 help_text=_("Udf fields"))
    udf_fields_udf_long_4502 = models.CharField(_("udf_fields_udf_long_4502"),null=True,max_length=10000,
                                                help_text=_("Udf fields udf long 4502"))
    impact_details = models.CharField(_("impact_details"),max_length=10000,null=True,
                                      help_text=_("Impact Details"))
    subcategory_name = models.CharField(_("subcategory_name"),max_length=10000,null=True,
                                        help_text=_("Subcategory name"))
    subcategory_id = models.IntegerField(_("subcategory_id"),null=True,
                                      help_text=_("Subcategory id"))
    email_cc = models.CharField(_("email_cc"),max_length=10000,null=True,
                                help_text=_("Email cc"))
    status_color = models.CharField(_("status_color"),max_length=10000,null=True,
                                    help_text=_("Status Color"))
    status_name = models.CharField(_("status_name"),max_length=10000,null=True,
                                   help_text=_("Status name"))
    status_id = models.IntegerField(_("status_id"),null=True,
                                 help_text=_("Status id"))
    template_name = models.CharField(_("template_name"),max_length=10000,null=True,
                                     help_text=_("Template name"))
    template_id = models.IntegerField(_("template_id"),null=True,
                                   help_text=_("Template id"))
    email_ids_to_notify = models.CharField(_("email_ids_to_notify"),max_length=10000,null=True,
                                           help_text=_("Email ids to notify"))
    request_type_name = models.CharField(_("request_type_name"),max_length=10000,null=True,
                                         help_text=_("Request type name"))
    request_type_id = models.IntegerField(_("request_type_id"),null=True,
                                       help_text=_("Request type id"))
    is_request_contract_applicable = models.BooleanField(_("is_request_contract_applicable"),null=True,
                                                      help_text=_("Request contrat applicable"))
    time_elapsed_display_value = models.DateTimeField(_("time_elapsed_display_value"),max_length=10000,null=True,blank=True,
                                                  help_text=_("Time elapsed display value"))
    time_elapsed_value = models.CharField(_("time_elapsed_value"),max_length=10000,null=True,
                                          help_text=_("Time elapsed value"))
    description = models.CharField(_("description"),max_length=10000,null=True,
                                   help_text=_("Description"))
    has_dependency = models.BooleanField(_("has_dependency"),null=True,
                                      help_text=_("Has Dependency"))
    closure_info_requester_ack_comments = models.CharField(_("closure_info_requester_ack_comments"),max_length=10000,
                                                           null=True,
                                                           help_text=_("Closure info requester ack comments"))
    closure_info_closure_code = models.CharField(_("closure_info_closure_code"),max_length=10000,null=True,
                                                 help_text=_("Closure info closure code"))
    closure_info_closure_comments = models.CharField(_("closure_info_closure_comments"),max_length=10000,null=True,
                                                     help_text=_("Closure info closure comments"))
    closure_info_signoff = models.CharField(_("closure_info_signoff"),max_length=10000,null=True,
                                            help_text=_("Closure info signoff"))
    closure_info_requester_ack_resolution = models.CharField(_("closure_info_requester_ack_resolution"),null=True,
                                                             max_length=10000,
                                                             help_text=_("Closure info requester ack resolution"))
    has_conversation = models.BooleanField(_("has_conversation"),null=True,
                                        help_text=_("Has conversation"))
    callback_url = models.CharField(_("callback_url"),max_length=10000,null=True,
                                    help_text=_("Callback url"))
    is_service_request = models.BooleanField(_("is_service_request"),null=True,
                                          help_text=_("Is service Request"))
    urgency_name = models.CharField(_("urgency_name"),max_length=10000,null=True,
                                    help_text=_("Urgency Name"))
    urgency_id = models.IntegerField(_("urgency_id"),null=True,
                                  help_text=_("Urgency Id"))
    is_shared = models.BooleanField(_("is_shared"),null=True,
                                 help_text=_("Is shared"))
    billing_status_billingstatusid = models.IntegerField(_("billing_status_billingstatusid"),null=True,
                                                      help_text=_("Billing status billingstatusid"))
    billing_status_billingstatusname = models.CharField(_("billing_status_billingstatusname"),max_length=10000,null=True,
                                                        help_text=_("Billing Status Billing Status Name"))
    accountcontract_serviceplan_id = models.IntegerField(_("accountcontract_serviceplan_id"),null=True,
                                                      help_text=_("Account contract serviceplan id"))
    accountcontract_isactivecontract = models.BooleanField(_("accountcontract_isactivecontract"),null=True,
                                                        help_text=_("Account contract is active contract"))
    accountcontract_contractnumber = models.CharField(_("accountcontract_contractnumber"),null=True,max_length=10000,
                                                      help_text=_("Account contract contract number"))
    accountcontract_contractid = models.IntegerField(_("accountcontract_contractid"),null=True,
                                                  help_text=_("Account contract contract id"))
    accountcontract_contractname = models.CharField(_("accountcontract_contractname"),max_length=10000,null=True,
                                                    help_text=_("Account contract contract name"))
    accountcontract_description = models.CharField(_("accountcontract_description"),max_length=10000,null=True,
                                                   help_text=_("Account contract description"))
    accountcontract_billunclosed = models.BooleanField(_("accountcontract_billunclosed"),null=True,
                                                    help_text=_("Account contract bill unclosed"))
    has_request_initiated_change = models.BooleanField(_("has_request_initiated_change"),null=True,
                                                    help_text=_("Has request initiated change"))
    request_template_task_ids = models.CharField(_("request_template_task_ids"),max_length=10000,null=True,
                                                 help_text=_("Request template task ids"))
    department_name = models.CharField(_("department_name"),max_length=10000,null=True,help_text=_("Department name"))
    department_id = models.IntegerField(_("department_id"),null=True,help_text=_("Department ID"))
    is_reopened = models.BooleanField(_("is_reopened"),null=True,help_text=_("Is reopenend"))
    has_draft = models.BooleanField(_("has_draft"),null=True,help_text=_("Has draft"))
    has_attachments = models.BooleanField(_("has_attachments"),null=True,
                                       help_text=_("Has attachments"))
    has_linked_requests = models.BooleanField(_("has_linked_requests"),null=True,
                                           help_text=_("Has linked requests"))
    is_overdue = models.BooleanField(_("is_overdue"),null=True,help_text=_("Is overdue"))
    technician_email_id = models.CharField(_("technician_email_id"),max_length=10000,null=True,
                                           help_text=_("Technician Email ID"))
    technician_name = models.CharField(_("technician_name"),max_length=10000,null=True,
                                       help_text=_("Technician name"))
    technician_mobile = models.CharField(_("technician_mobile"),max_length=10000,null=True,
                                         help_text=_("Technician Mobile"))
    technician_id = models.IntegerField(_("technician_id"),null=True,help_text=_("Technician id"))
    technician_status = models.CharField(_("technician_status"),max_length=10000,null=True,
                                         help_text=_("Technician Status"))
    is_billable = models.BooleanField(_("is_billable"),null=True,help_text=_("Is billable"))
    has_problem = models.BooleanField(_("has_problem"),null=True,help_text=_("Has Problem"))
    due_by_time = models.DateTimeField(_("due_by_time"),max_length=10000,null=True,blank=True,help_text=_("Due by time"))
    is_fcr = models.BooleanField(_("is_fcr"),null=True,help_text=_("Is fcr"))
    has_project = models.BooleanField(_("has_project"),null=True,
                                   help_text=_("Has Project"))
    site_name = models.CharField(_("site_name"),max_length=10000,null=True,
                                 help_text=_("Site Name"))
    site_id = models.IntegerField(_("site_id"),null=True,
                               help_text=_("Site ID"))
    is_first_response_overdue = models.BooleanField(_("is_first_response_overdue"),null=True,
                                                 help_text=_("Is first response overdue"))
    completed_time_display_value = models.DateTimeField(_("completed_time_display_value"),max_length=10000,null=True,blank=True,
                                                    help_text=_("Completed time display value"))
    completed_time_value = models.CharField(_("completed_time_value"),max_length=10000,null=True,
                                            help_text=_("Completed time value"))
    category_name = models.CharField(_("category_name"),max_length=10000,null=True,help_text=_("Category name"))
    category_id = models.IntegerField(_("category_id"),null=True,help_text=_("Category id"))
    account_name = models.CharField(_("account_name"),max_length=10000,null=True,
                                    help_text=_("Account name"))
    account_id = models.IntegerField(_("account_id"),null=True,help_text=_("Account id"))
    subcategory = models.CharField(_("subcategory"),max_length=10000,null=True,help_text=_("Subcategory"))
    closure_info_closure_code_name = models.CharField(_("closure_info_closure_code_name"),max_length=10000,null=True,
                                                      help_text=_("Closure info closure code name"))
    closure_info_closure_code_id = models.IntegerField(_("closure_info_closure_code_id"),null=True,
                                                    help_text=_("Closure info closure code id"))
    mode = models.CharField(_("mode"),max_length=10000,null=True,help_text=_("Mode"))
    item = models.CharField(_("item"),max_length=10000,null=True,help_text=_("Item"))
    level_name = models.CharField(_("level_name"),max_length=10000,null=True,help_text=_("Level Name"))
    level_id = models.IntegerField(_("level_id"),null=True,help_text=_("Level id"))
    udf_fields_udf_sline_5401 = models.CharField(_("udf_fields_udf_sline_5401"),max_length=10000,null=True,
                                                 help_text=_("UDF Fields udf sline 5401"))
    udf_fields_udf_long_3302 = models.CharField(_("udf_fields_udf_long_3302"),max_length=10000,null=True,
                                                help_text=_("UDF Fields udf sline 3302"))
    subject = models.CharField(_("subject"),max_length=10000,null=True,help_text=_("Subject"))
    created_at = models.DateTimeField(_("created at"), default=datetime.now, help_text=_("created at"))
    soar_id = models.IntegerField(_("soar_id"),null=True,help_text=_("Soar id"))

