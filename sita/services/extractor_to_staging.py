from datetime import datetime
from sita.models import EXTRACTOR_SOAR,STG_SOAR,EXTRACTOR_ITSM,EXTRACTOR_SIEM,STG_SIEM,FACT_OEI,Audit_SOAR_EXTRACTOR, \
    Audit_SIEM_EXTRACTOR,Audit_ITSM_EXTRACTOR
from sita.models.audit_siem_stg import Audit_SIEM_STG
from sita.models.audit_soar_stg import Audit_SOAR_STG
from sita.models.audit_itsm_stg import Audit_ITSM_STG


class ExtractorToStgService:
    @staticmethod
    def extractor_to_stg_soar():
        """
         Function to create and update stage_soar table data
        """
        now = datetime.now()
        end_time = datetime.now()
        status = "Failed"
        try:
            audit = Audit_SOAR_EXTRACTOR.objects.filter(status="Success").last()
            start_date = audit.start_date
            last_date = audit.end_date
            queryset = EXTRACTOR_SOAR.objects.filter(created_at__gte=start_date, created_at__lte=last_date)
            a = []
            for row in queryset:
                closing_time = int(row.ClosingTime)
                soar = {
                    "SOAR_ID": int(row.SOAR_ID),
                    "AssignedUser": row.AssignedUser,
                    "Title": row.Title,
                    "Time": row.Time,
                    "Tags": row.Tags,
                    "Products": row.Products,
                    "Incident": row.Incident,
                    "Suspicious": row.Suspicious,
                    "Important": row.Important,
                    "Ports": int(row.Ports),
                    "Outcomes": row.Outcomes,
                    "Status": row.Status,
                    "Environment": row.Environment,
                    "Priority": row.Priority,
                    "Stage": row.Stage,
                    "TicketIDs": row.TicketIDs,
                    "ClosingTime": datetime.fromtimestamp(closing_time/1000),
                    "Sources": row .Sources,
                    "Reason": row.Reason,
                    "RootCause": row.RootCause,
                    "Case_id": row.Case_id,
                    "AlertsCount": row.AlertsCount
                }

                soar_id = int(row.SOAR_ID)
                # this line will create soar data according to given soar dict
                a = STG_SOAR.objects.update_or_create(defaults=soar, SOAR_ID=soar_id)
            end_time = datetime.now()
            status = "Success"
            return a
        except Exception as e:
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
            audit = Audit_SOAR_STG.objects.create(**audit_dict)
            return audit_dict

    @staticmethod
    def extractor_to_stg_siem():
        """
         Function to create and update stage_soar table data
        """
        now = datetime.now()
        end_time = datetime.now()
        status = "Failed"
        try:
            audit = Audit_SIEM_EXTRACTOR.objects.filter(status="Success").last()
            start_date = audit.start_date
            last_date = audit.end_date
            queryset = EXTRACTOR_SIEM.objects.filter(created_at__gte=start_date, created_at__lte=last_date).values()
            final_siem = []
            for query in queryset:
                siem = {
                    "last_persisted_time": datetime.fromtimestamp(int(query.get("last_persisted_time"))/1000) if query.get("last_persisted_time") is not None else None,
                    "username_count": query.get("username_count", None),
                    "description": query.get('description', None),
                    "rules": query.get('rules', None),
                    "event_count": query.get('event_count', None),
                    "flow_count": query.get('flow_count', None),
                    "assigned_to": query.get('assigned_to', None),
                    "security_category_count": query.get('security_category_count', None),
                    "follow_up": query.get('follow_up', None),
                    "source_address_ids": query.get('local_destination_address_ids', None),
                    "source_count": query.get('source_count', None),
                    "inactive": query.get('inactive', None),
                    "protected": query.get('protected', None),
                    "closing_user": query.get('closing_user', None),
                    "destination_networks": query.get('destination_networks', None),
                    "source_network": query.get('source_network', None),
                    "category_count": query.get('category_count', None),
                    "close_time": datetime.fromtimestamp(int(query.get("close_time"))/1000) if query.get("close_time") is not None else None,
                    "remote_destination_count": query.get('remote_destination_count', None),
                    "start_datetime": datetime.fromtimestamp(int(query.get("start_time"))/1000) if query.get("start_time") is not None else None,
                    "magnitude": query.get('magnitude', None),
                    "last_updated_datetime": datetime.fromtimestamp(int(query.get("last_updated_datetime"))/1000) if query.get("last_updated_datetime") is not None else None,
                    "credibility": query.get('credibility', None),
                    "id": query.get('id', None),
                    "categories": query.get('', None),
                    "severity": query.get('severity', None),
                    "policy_category_count": query.get('policy_category_count', None),
                    "log_sources": query.get('', None),
                    "closing_reason_id": query.get('closing_reason_id', None),
                    "device_count": query.get('device_count', None),
                    "first_persisted_time": datetime.fromtimestamp(int(query.get("first_persisted_time"))/1000) if query.get("first_persisted_time") is not None else None,
                    "offense_type": query.get('offense_type', None),
                    "relevance": query.get('relevance', None),
                    "domain_id": query.get('domain_id', None),
                    "offense_source": query.get('offense_source', None),
                    "local_destination_address_ids": query.get('local_destination_address_ids', None),
                    "local_destination_count": query.get('local_destination_count', None),
                    "status": query.get('status', None),
                    "rule_details": query.get('rule_details', None),
                    "seim_id": query.get('siem_id', None),
                }
                final_siem.append(siem)
                values = STG_SIEM.objects.update_or_create(defaults=siem, seim_id=query.get('siem_id'))
                # this line will create soar data according to given soar dict
                end_time = datetime.now()
                status = "Success"
            return status
        except Exception as e:
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
            audit = Audit_SIEM_STG.objects.create(**audit_dict)
            return audit_dict

    @staticmethod
    def extractor_to_stg_itsm():
        now = datetime.now()
        end_time = datetime.now()
        status = "Failed"
        try:
            audit = Audit_ITSM_EXTRACTOR.objects.filter(status="Success").last()
            start_date = audit.start_date
            last_date = audit.end_date
            queryset = EXTRACTOR_ITSM.objects.filter(created_at__gte=start_date, created_at__lte=last_date).values()
            for query in queryset:
                if query.get('assets'):
                    final_itsm = []
                    for asset in list(eval(query.get('assets'))):
                        itsm = {
                            "resolution_submitted_on_display_value": query.get("resolution_submitted_on_display_value", None),
                            "resolution_submitted_on_value": query.get("resolution_submitted_on_value", None),
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
                            "assigned_time_display_value": query.get("assigned_time_display_value", None),
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
                            "created_time_display_value": query.get("username_count", None),
                            "created_time_value": query.get("created_time_value", None),
                            "has_resolution_attachments": query.get("has_resolution_attachments", None),
                            "approval_status": query.get("approval_status", None),
                            "impact_name": query.get("impact_name", None),
                            "impact_id": query.get("impact_id", None),
                            "service_category_name": query.get("service_category_name", None),
                            "service_category_id": query.get("service_category_id", None),
                            "sla_name": query.get("sla_name", None),
                            "sla_id": query.get("sla_id", None),
                            "resolved_time_display_value": query.get("resolved_time_display_value", None),
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
                            "last_updated_time_display_value": query.get("last_updated_time_display_value", None),
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
                            "time_elapsed_display_value": query.get("time_elapsed_display_value", None),
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
                            "completed_time_display_value": query.get("completed_time_display_value", None),
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
                            "subject": query.get("subject", None)
                        }
                        final_itsm.append(itsm)
                        a = FACT_OEI.objects.create(**itsm)
                        # this line will create soar data according to given soar dict
                        end_time = datetime.now()
                        status = "Success"
            return status
        except Exception as e:
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
