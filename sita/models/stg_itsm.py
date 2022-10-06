from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords


class STG_ITSM(models.Model):
    """
    Model to hold data for ITSM data
    """
    class PriorityValue(models.TextChoices):
        Low = "Low", _("Low")
        Medium = "Medium", _("Medium")
        High = "High", _("High")

    class ModeOfRequest(models.TextChoices):
        Email = "Email", _("Email")
        Call = "Call", _("Call")
        Message = "Message", _("Message")
        Whatsapp = "Whatsapp", _("Whatsapp")

    RequestID = models.CharField(_("RequestID"), max_length=200, null=True, help_text=_("Request Id"))
    Request_mode = models.CharField(_("Request_mode"), max_length=200, choices=ModeOfRequest.choices, null=True,
                                    help_text="Request Mode")
    Cluster = models.CharField(_("Cluster"), max_length=200, null=True, help_text=_("Cluster"))
    Applicant = models.CharField(_("Applicant"), max_length=200, null=True, help_text=_("Applicant"))
    Department = models.CharField(_("Department"), max_length=200, null=True, help_text=_("Department"))
    Category = models.CharField(_("Category"), max_length=200, null=True, help_text=_("Category"))
    Subcategory = models.CharField(_("Subcategory"), max_length=200, null=True, help_text=_("Sub Category"))
    Article = models.CharField(_("Article"), max_length=200, null=True, help_text=_("Article"))
    Affair = models.CharField(_("Affair"), max_length=200, null=True, help_text=_("Affair"))
    Created_by = models.CharField(_("Created_by"), max_length=200, null=True, help_text=_("Created By"))
    Urgency = models.CharField(_("Urgency"), max_length=200, choices=PriorityValue.choices, null=True,
                               help_text=_("Urgency"))
    Impact = models.CharField(_("Impact"), max_length=200, choices=PriorityValue.choices, null=True,
                              help_text=_("Impact"))
    RequestType = models.CharField(_("RequestType"), max_length=200, null=True, help_text=_("Request Type"))
    Technician = models.CharField(_("Technician"), max_length=2000, null=True, help_text=_("Technician"))
    Description = models.CharField(_("Description"), max_length=15000, null=True, help_text=_("Description"))
    Site = models.CharField(_("Site"), max_length=200, null=True, help_text=_("Site"))
    Region = models.CharField(_("Region"), max_length=200, null=True, help_text=_("Region"))
    Approval_Status = models.CharField(_("Approval_Status"), max_length=200, null=True, help_text=_("Approval Status"))
    Request_closing_code = models.CharField(_("Request_closing_code"), max_length=200, null=True,
                                            help_text=_("Request Closing Code"))
    Request_Closure_Comments = models.CharField(_("Request_Closure_Comments"), max_length=200, null=True,
                                                help_text=_("Request_Closure_Comments"))
    service_category = models.CharField(_("service_category"), max_length=200, null=True,
                                        help_text=_("Service Category"))
    Priority = models.CharField(_("Priority"), max_length=200, choices=PriorityValue.choices, null=True,
                                help_text=_("Priority"))
    Level = models.CharField(_("Level"), max_length=200, null=True, help_text=_("Level"))
    Asset_Name = models.CharField(_("Asset_Name"), max_length=200, null=True, help_text=_("Asset Name"))
    Application_Status = models.CharField(_("Application_Status"), max_length=200, null=True,
                                          help_text=_("Application status"))
    Pending_status = models.BooleanField(_("Pending_status"), null=True, help_text=_("Pending Status"))
    CreatedTime = models.DateTimeField(_("CreatedTime"), max_length=200, null=True,
                                       help_text=_("Created Time"))
    Answer_date = models.DateTimeField(_("Answer_date"), max_length=200, null=True, help_text=_("Answer Date"))
    Expiration_time = models.DateTimeField(_("Expiration_time"), max_length=200, null=True,
                                           help_text=_("Expiration Time"))
    Ending_time = models.DateTimeField(_("Ending_time"), max_length=200, null=True,
                                       help_text=_("Ending Time"))
    Time_elapsed = models.CharField(_("Time_elapsed"), max_length=200, null=True,
                                        help_text=_("Time Elapsed"))
    Expired_status = models.BooleanField(_("Expired_status"), null=True, help_text=_("Expire Status"))
    Itsm_id = models.CharField(_("Itsm_id"), max_length=200, null=True, help_text=_("ITSM Id"))
    Subject = models.CharField(_("Subject"), max_length=200, null=True, help_text=_("Subject"))
    RequestStatus = models.CharField(_("RequestStatus"), max_length=200, null=True, help_text="Request Status")
    Account = models.CharField(_("Account"), max_length=200, null=True, help_text="Account")
    Resolution = models.CharField(_("Resolution"), max_length=10000, null=True, help_text="Resolution")
    reopened = models.CharField(_("Reopened"), null=True, max_length=2000, help_text="Reopened")
    RCF = models.CharField(_("RCF"), max_length=200, null=True, help_text="RCF")
    User_On_Behalf_Of_OBO = models.CharField(_("User_On_Behalf_Of_OBO"), max_length=200, null=True,
                                             help_text=_("User_On_Behalf_Of_OBO"))
    total_cost = models.CharField(_("Total_cost"), max_length=200, null=True, help_text=_("Total_cost"))
    Exchanged_Service = models.CharField(_("Exchanged_Service"), max_length=2000, null=True,
                                         help_text=_("Exchanged_Service"))
    Sale_order = models.CharField(_("Sale_order"), max_length=200, null=True, help_text=_("Sale_order"))
    number_of_services = models.CharField(_("Number_of_Services"), null=True, max_length=200,
                                          help_text=_("Number_of_Services"))
    Solicitant_area = models.CharField(_("Solicitant_area"), max_length=200, null=True,
                                       help_text=_("Solicitant_area"))
    Complexity = models.CharField(_("Complexity"), max_length=200, null=True, help_text=_("Complexity"))
    Type = models.CharField(_("Type"), max_length=200, null=True, help_text=_("Type"))
    Opportunity_Status = models.CharField(_("Opportunity_Status"), max_length=200, null=True,
                                          help_text=_("Opportunity_Status"))
    Qualys_first_time_detected = models.CharField(_("Qualys_first_time_detected"), max_length=200, null=True,
                                                  help_text=_("qualys_first_time_detected"))
    Qualys_url = models.CharField(_("Qualys_url"), max_length=200, null=True, help_text=_("qualys_url"))
    Qualys_last_time_detected = models.CharField(_("Qualys_last_time_detected"), max_length=200, null=True,
                                                 help_text=_("Iqualys_last_time_detected"))
    Qualys_last_time_tested = models.CharField(_("Qualys_last_time_tested"), max_length=200, null=True,
                                               help_text=_("qualys_last_time_tested"))
    Qualys_category = models.CharField(_("Qualys_category"), max_length=200, null=True,
                                       help_text=_("Iqualys_category"))
    Qualys_severity = models.CharField(_("Qualys_severity"), max_length=200, null=True, help_text=_("qualys_severity"))
    Qualys_group = models.CharField(_("Qualys_group"), max_length=200, null=True, help_text=_("qualys_group"))
    Qualys_payload_method = models.CharField(_("Qualys_payload_method"), max_length=200, null=True,
                                             help_text=_("qualys_payload_method"))
    Qualys_payload_response = models.CharField(_("Qualys_payload_response"), max_length=200, null=True,
                                               help_text=_("qualys_payload_response"))
    Qualys_state = models.CharField(_("Qualys_state"), max_length=200, null=True, help_text=_("qualys_state"))
    Qualys_owasp_name = models.CharField(_("Qualys_owasp_name"), max_length=200, null=True,
                                         help_text=_("qualys_owasp_name"))
    Qualys_impact = models.CharField(_("Qualys_impact"), max_length=200, null=True, help_text=_("Iqualys_impact"))
    Qualys_owasp = models.CharField(_("Qualys_owasp"), max_length=200, null=True, help_text=_("qualys_owasp"))
    Qualys_solution = models.CharField(_("Qualys_solution"), max_length=200, null=True, help_text=_("qualys_solution"))
    Qualys_cvss_base = models.CharField(_("Qualys_cvss_base"), max_length=200, null=True, help_text=_("qualys_cvss_base"))
    Qualys_cvss_temporary = models.CharField(_("Qualys_cvss_temporary"), max_length=200, null=True,
                                             help_text=_("qualys_cvss_temporary"))
    Qualys_id = models.CharField(_("Qualys_id"), max_length=200, null=True, help_text=_("qualys_id"))
    Sensor = models.CharField(_("Sensor"), max_length=200, null=True, help_text=_("Sensor"))
    ID = models.IntegerField(_("ID"), null=True, help_text=_("Id"))
    Case_With_Manufacturer = models.CharField(_("Case_With_Manufacturer"), max_length=200, null=True,
                                              help_text=_("Case_With_Manufacturer"))
    Spare_Parts_Stock_Delivery_Date = models.CharField(_("Spare_Parts_Stock_Delivery_Date"), max_length=200, null=True,
                                                       help_text=_("Spare_Parts_Stock_Delivery_Date"))
    Onsite_engineer_request_date = models.CharField(_("Case_With_Manufacturer"), max_length=200, null=True,
                                                    help_text=_("Onsite_engineer_request_date"))
    Onsite_care_date = models.CharField(_("Case_With_Manufacturer"), max_length=200, null=True,
                                        help_text=_("Onsite_care_date"))
    Onsite_service_SLA = models.CharField(_("Onsite_service_SLA"), max_length=200, null=True,
                                          help_text=_("Onsite_service_SLA"))
    Neutralization_SLA = models.CharField(_("Neutralization_SLA"), max_length=200, null=True,
                                          help_text=_("Neutralization_SLA"))
    Fault_Neutralization_Date = models.CharField(_("Fault_Neutralization_Date"), max_length=200, null=True,
                                                 help_text=_("Fault_Neutralization_Date"))
    Telephone_notification_date = models.CharField(_("Telephone_notification_date"), max_length=200, null=True,
                                                   help_text=_("Telephone_notification_date"))
    SLA_Service_time_for_remote_connection = models.CharField(_("SLA_Service_time_for_remote_connection"), max_length=200, null=True,
                                                              help_text=_("SLA_Service_time_for_remote_connection"))
    SLA_Stock_of_Spare_Parts = models.CharField(_("SLA_Stock_of_Spare_Parts"), max_length=200, null=True,
                                                help_text=_("SLA_Stock_of_Spare_Parts"))
    Hardware_Damage_Confirmation_Date_Manufacturer = models.CharField(_("Hardware_Damage_Confirmation_Date_Manufacturer"), max_length=200, null=True,
                                                                      help_text=_("Hardware_Damage_Confirmation_Date"))
    SLA_Spare_Parts_Stock_Delivery_Time = models.DateTimeField(_("SLA_Spare_Parts_Stock_Delivery_Time"), null=True,
                                                               help_text=_("SLA_Spare_Parts_Stock_Delivery_Time"))
    Contract_start_date = models.CharField(_("Contract_start_date"), max_length=200, null=True,
                                           help_text=_("Contract_start_date"))
    Bill = models.CharField(_("Bill"), max_length=200, null=True, help_text=_("Bill"))
    Response_due_time = models.DateTimeField(_("Response_due_time"), null=True, help_text=_("Response Due Time"))
    First_Responder_Status_Expired = models.BooleanField(_("First_Responder_Status_Expired"), null=True,
                                                         help_text=_("First sponder status expired"))
    Last_update_time = models.DateTimeField(_("Last_update_time"), null=True, help_text=_("Last_update_time"))
    Resolution_time = models.DateTimeField(_("Resolution_time"), null=True, help_text=_("Resolution_time"))
    VIP_user = models.BooleanField(_("VIP_user"), null=True, help_text=_("VIP_user"))
    SIEM_id = models.CharField(_("SIEM_id"), null=True, max_length=200, help_text=_("SIEM Id"))
    sla_name = models.CharField(_("sla_name"), null=True, max_length=200, help_text=_("sla_name"))
    is_overdue = models.CharField(_("is_overdue"), max_length=200, help_text=_("Overdue Status"), null=True)
    category_id = models.CharField(_("sla_id"), null=True, max_length=200, help_text=_("sla_id"))
    submitted_by = models.CharField(_("submitted_by"), null=True, max_length=200, help_text=_("submmited by"))
    location_name = models.CharField(_("location_name"), null=True, max_length=200, help_text=_("location name"))
    reply = models.CharField(_("replys"), max_length=200, help_text=_("Replies"), null=True)
    Child_CI_type = models.CharField(_("Child ci name"), max_length=200, null=True, help_text=_("Asset Affected"))
    assigned_time = models.DateTimeField(_("assigned_time"), max_length=200, null=True, help_text=_("Time send mail"))
    sla_completion_time = models.CharField(_("sla_completion_time"), max_length=200, null=True,
                                           help_text=_("sla_completion_time"))
    first_response_time_id = models.CharField(_("first_response_time_id"), null=True, max_length=200,
                                              help_text=_("first_response_time_id"))
    first_response_time = models.CharField(_("first_response_time"), null=True, max_length=200,
                                           help_text=_("first_response_time"))
    response_time_id = models.CharField(_("response_time_id"), null=True, max_length=200,
                                        help_text=_("response_time_id"))
    false_positives_id = models.CharField(_("false_positives_id"), null=True, max_length=200,
                                          help_text=_("false_positives_id"))
    reopened_id = models.CharField(_("reopened_id"), null=True, max_length=200, help_text=_("reopened_id"))
    false_positives = models.CharField(_("false_positives"), null=True, max_length=200,
                                       help_text=_("false_positives"))
    SOAR_ID = models.CharField(_("Soar_id"), null=True, max_length=200, help_text=_("soar_id"))
    due_by_time = models.CharField(_("Due_by_Time"), null=True, max_length=200, help_text=_("Due_by_Time"))
    is_first_response_overdue = models.CharField(_("Is_First_Respose_Overdue"), null=True, max_length=200,
                                                 help_text=_("Is_First_Response_Overdue"))
    target = models.CharField(_("target"), null=True, max_length=200, help_text=_("Target"))
    group = models.CharField(_("group"), null=True, max_length=200, help_text=_("group"))
    resolved_time = models.CharField(_("resolved_time"), max_length=200, null=True, help_text=_("resolved_time"))
    response_time = models.CharField(_("reesponse_time"), max_length=200, null=True, help_text=_("response_time"))

    # AuditLog table config
    # history = HistoricalRecords(_("stg_itsm_history"), table_name="stg_itsm_history")
