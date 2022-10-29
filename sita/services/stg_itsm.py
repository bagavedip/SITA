from datetime import datetime
import os
import requests
import time
from django.utils.timezone import make_aware
from django.utils import timezone
import pytz
IST = pytz.timezone('Asia/Kolkata')

from urllib.parse import urljoin

from sita.models import STG_ITSM, EXTRACTOR_ITSM
from sita.models.audit_itsm_extractor import Audit_ITSM
from sita.models.audit_itsm_stg import Audit_ITSM_STG


# Remove warnings messages
requests.packages.urllib3.disable_warnings()


class ITSMServices:
   
    @staticmethod
    def itsm():
        now = datetime.now()
        end_time = timezone.now()
        status = "Failed"
        try:
            audit = Audit_ITSM.objects.filter(status="Success").last()
            print('audit is', audit)
            start_date = audit.start_date
            print('start date is', start_date)
            last_date = audit.end_date
            print('end date is', last_date)
            queryset = EXTRACTOR_ITSM.objects.filter(created_at__gte=start_date, created_at__lte=last_date).values()

            for query in queryset:
                final_itsm = []
                for asset in list(eval(query.get('assets'))):
                    format =  "%b %d, %Y %H:%M %p"  
                    itsm = {
                        "resolution_submitted_on_display_value": datetime.strptime(query.get("resolution_submitted_on_display_value"), format) if query.get("resolution_submitted_on_display_value") is not None else None,
                        "resolution_submitted_on_value":query.get("resolution_submitted_on_value", None) ,
                        "resolution_submitted_by_email_id": query.get("resolution_submitted_by_email_id", None),
                        "resolution_submitted_by_name": query.get("resolution_submitted_by_name", None),
                        "resolution_submitted_by_mobile": query.get("resolution_submitted_by_mobile", None),
                        "resolution_submitted_by_is_vipuser": query.get("resolution_submitted_by_is_vipuser", None),
                        "resolution_submitted_by_id": query.get("resolution_submitted_by_id", None),
                        "resolution_submitted_by_status": query.get("resolution_submitted_by_status", None),
                        "resolution_resolution_attachments": query.get("resolution_resolution_attachments", None),
                        "resolution_content": query.get("resolution_content", None),
                        "linked_to_request": query.get("linked_to_request", None),
                        "mode_name": query.get("mode_name", None),
                        "mode_id": query.get("mode_id", None),
                        "lifecycle": query.get("lifecycle", None),
                        "assets": asset,
                        "is_trashed": query.get("is_trashed", None),
                        "itsm_id": query.get("itsm_id", None),
                        "assigned_time_display_value": datetime.strptime(query.get("assigned_time_display_value"), format) if query.get("assigned_time_display_value") is not None else None,
                        "assigned_time_value": query.get("assigned_time_value", None),
                        "group_name": query.get("group_name", None),
                        "group_id": query.get("group_id", None),
                        "requester_email_id": query.get("requester_email_id", None),
                        "requester_name": query.get("requester_name", None),
                        "requester_mobile": query.get("requester_mobile", None),
                        "requester_is_vipuser": query.get("requester_is_vipuser", None),
                        "requester_id": query.get("requester_id", None),
                        "requester_status": query.get("requester_status", None),
                        "email_to": query.get("email_to", None),
                        "created_time_display_value": datetime.strptime(query.get("created_time_display_value"), format) if query.get("created_time_display_value") is not None else None,
                        "created_time_value": query.get("created_time_value", None),
                        "has_resolution_attachments": query.get("has_resolution_attachments", None),
                        "approval_status": query.get("approval_status", None),
                        "impact_name": query.get("impact_name", None),
                        "impact_id": query.get("impact_id", None),
                        "service_category_name": query.get("service_category_name", None),
                        "service_category_id": query.get("service_category_id", None),
                        "sla_name": query.get("sla_name", None),
                        "sla_id": query.get("sla_id", None),
                        "resolved_time_display_value": datetime.strptime(query.get("resolved_time_display_value"), format) if query.get("resolved_time_display_value") is not None else None,
                        "resolved_time_value": query.get("resolved_time_value", None),
                        "priority_color": query.get("priority_color", None),
                        "priority_name": query.get("priority_name", None),
                        "priority_id": query.get("priority_id", None),
                        "created_by_email_id": query.get("created_by_email_id", None),
                        "created_by_name": query.get("created_by_name", None),
                        "created_by_mobile": query.get("created_by_mobile", None),
                        "created_by_is_vipuser": query.get("created_by_is_vipuser", None),
                        "created_by_id": query.get("created_by_id", None),
                        "created_by_status": query.get("created_by_status", None),
                        "last_updated_time_display_value": datetime.strptime(query.get("last_updated_time_display_value"), format) if query.get("last_updated_time_display_value") is not None else None,
                        "last_updated_time_value": query.get("last_updated_time_value", None),
                        "has_notes": query.get("has_notes", None),
                        "udf_fields_udf_sline_4501": query.get("udf_fields_udf_sline_4501", None),
                        "udf_fields_udf_long_4502": query.get("udf_fields_udf_long_4502", None),
                        "impact_details": query.get("impact_details", None),
                        "subcategory_name": query.get("subcategory_name", None),
                        "subcategory_id": query.get("subcategory_id", None),
                        "email_cc": query.get("email_cc", None),
                        "status_color": query.get("status_color", None),
                        "status_name": query.get("status_name", None),
                        "status_id": query.get("status_id", None),
                        "template_name": query.get("template_name", None),
                        "template_id": query.get("template_id", None),
                        "email_ids_to_notify": query.get("email_ids_to_notify", None),
                        "request_type_name": query.get("request_type_name", None),
                        "request_type_id": query.get("request_type_id", None),
                        "is_request_contract_applicable": query.get("is_request_contract_applicable", None),
                        "time_elapsed_display_value": datetime.strptime(query.get("time_elapsed_display_value"), format) if query.get("time_elapsed_display_value") is not None else None,
                        "time_elapsed_value": query.get("time_elapsed_value", None),
                        "description": query.get("description", None),
                        "has_dependency": query.get("has_dependency", None),
                        "closure_info_requester_ack_comments": query.get("closure_info_requester_ack_comments", None),
                        "closure_info_closure_code": query.get("closure_info_closure_code", None),
                        "closure_info_closure_comments": query.get("closure_info_closure_comments", None),
                        "closure_info_signoff": query.get("closure_info_signoff", None),
                        "closure_info_requester_ack_resolution": query.get("closure_info_requester_ack_resolution", None),
                        "has_conversation": query.get("has_conversation", None),
                        "callback_url": query.get("callback_url", None),
                        "is_service_request": query.get("is_service_request", None),
                        "urgency_name": query.get("urgency_name", None),
                        "urgency_id": query.get("urgency_id", None),
                        "is_shared": query.get("is_shared", None),
                        "billing_status_billingstatusid": query.get("billing_status_billingstatusid", None),
                        "billing_status_billingstatusname": query.get("billing_status_billingstatusname", None),
                        "accountcontract_serviceplan_id": query.get("accountcontract_serviceplan_id", None),
                        "accountcontract_isactivecontract": query.get("accountcontract_isactivecontract", None),
                        "accountcontract_contractnumber": query.get("accountcontract_contractnumber", None),
                        "accountcontract_contractid": query.get("accountcontract_contractid", None),
                        "accountcontract_contractname": query.get("accountcontract_contractname", None),
                        "accountcontract_description": query.get("accountcontract_description", None),
                        "accountcontract_billunclosed": query.get("accountcontract_billunclosed", None),
                        "has_request_initiated_change": query.get("has_request_initiated_change", None),
                        "request_template_task_ids": query.get("request_template_task_ids", None),
                        "department_name": query.get("department_name", None),
                        "department_id": query.get("department_id", None),
                        "is_reopened": query.get("is_reopened", None),
                        "has_draft": query.get("has_draft", None),
                        "has_attachments": query.get("has_attachments", None),
                        "has_linked_requests": query.get("has_linked_requests", None),
                        "is_overdue": query.get("is_overdue", None),
                        "technician_email_id": query.get("technician_email_id", None),
                        "technician_name": query.get("technician_name", None),
                        "technician_mobile": query.get("technician_mobile", None),
                        "technician_id": query.get("technician_id", None),
                        "technician_status": query.get("technician_status", None),
                        "is_billable": query.get("is_billable", None),
                        "has_problem": query.get("has_problem", None),
                        "due_by_time": query.get("due_by_time", None),
                        "is_fcr": query.get("is_fcr", None),
                        "has_project": query.get("has_project", None),
                        "site_name": query.get("site_name", None),
                        "site_id": query.get("site_id", None),
                        "completed_time_display_value": datetime.strptime(query.get("completed_time_display_value"), format) if query.get("completed_time_display_value") is not None else None,
                        "completed_time_value": query.get("completed_time_value", None),
                        "category_name":query.get("category_name", None),
                        "category_id": query.get("category_id", None),
                        "account_name": query.get("account_name", None),
                        "account_id": query.get("account_id", None),
                        "subcategory": query.get("subcategory", None),
                        "closure_info_closure_code_name": query.get("closure_info_closure_code_name", None),
                        "closure_info_closure_code_id": query.get("closure_info_closure_code_id", None),
                        "mode": query.get("mode", None),
                        "item": query.get("item", None),
                        "level_name": query.get("level_name", None),
                        "level_id": query.get("level_id", None),
                        "udf_fields_udf_sline_5401": query.get("udf_fields_udf_sline_5401", None),
                        "udf_fields_udf_long_3302": query.get("udf_fields_udf_long_3302", None),
                        "subject":query.get("subject", None),
                        "soar_id":query.get("subject").split('-')[0].split(':')[1] if query.get("subject").split('-')[0].split(':')[1] is not None else None
                    }

                    final_itsm.append(itsm)
                    a = STG_ITSM.objects.update_or_create(defaults=itsm, itsm_id=query.get('itsm_id'), assets = asset)
                    # this line will create soar data according to given soar dict
                    end_time = datetime.now()
                    status = "Success"
            return status
        except Exception as e:
            print('exception is', e)
            end_time = datetime.now()
            status = "Failed"
            return e
        finally:
            # we are creating Audit record in this block
            audit_dict = {
                "start_date": now,
                "end_date": end_time,
                "status": status
            }
            audit = Audit_ITSM_STG.objects.create(**audit_dict)
            return audit_dict



