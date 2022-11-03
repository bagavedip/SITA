import requests
import datetime
from sita.models.audit_itsm_extractor import Audit_ITSM_EXTRACTOR
from sita.models.extractor_itsm import EXTRACTOR_ITSM


class ITSMServices:
    """
    Function used to Extract ITSM data
    """
    @staticmethod
    def double_nested_data(data, key1, key2):
        """
         function used to check double nested dict in itsm url if any dict has none get none
        """
        return data.get(key1, {}).get(key2) if data.get(key1) is not None else None

    @staticmethod
    def triple_nested_data(data, key1, key2, key3):
        """
         function used to check triple neted dict in itsm url if any dict has none get none
        """
        return data.get(key1, {}).get(key2, {}).get(key3) if data.get(key1) is not None else None

    @staticmethod
    def itsm_dump():
        """
         function to get all record from itsm to extractor table
        """
        start_time = datetime.datetime.now()
        end_time = datetime.datetime.now()
        status = "Failed"
        try:
            url = 'https://192.168.201.20/api/v3/requests'
            headers = {"technician_key": "DCFFE887-4B30-4E7E-9608-6379B483414E"}
            response = requests.get(url, headers=headers, verify=False)
            
            # this line will give us 'requests' record from url 
            data = response.json().get('requests')
            numbers = []
            a = []
            for keys in data:
                # fetch key in requests data for fetch single record
                num = keys.get('id')
                numbers.append(num)
                for n in numbers:
                    url = "https://192.168.201.20/api/v3/requests/" + str(n)
                    headers = {"technician_key": "DCFFE887-4B30-4E7E-9608-6379B483414E"}
                    response = requests.get(url, headers=headers, verify=False)

                    # this line will give us 'request' record from url 
                    data = response.json().get('request')
                    itsm = {
                        "resolution_submitted_on_display_value": ITSMServices.triple_nested_data(data, 'resolution', 'submitted_on',
                                                                                        'display_value'),
                        "resolution_submitted_on_value": ITSMServices.triple_nested_data(data, 'resolution', 'submitted_on', 'value'),
                        "resolution_submitted_by_email_id": ITSMServices.triple_nested_data(data, 'resolution', 'submitted_on', 'email_id'),
                        "resolution_submitted_by_name": ITSMServices.triple_nested_data(data, 'resolution', 'submitted_on', 'name'),
                        "resolution_submitted_by_mobile": ITSMServices.triple_nested_data(data, 'resolution', 'submitted_on', 'mobile'),
                        "resolution_submitted_by_is_vipuser": ITSMServices.triple_nested_data(data, 'resolution', 'submitted_on',
                                                                                     'is_vipuser'),
                        "resolution_submitted_by_id": ITSMServices.triple_nested_data(data, 'resolution', 'submitted_on', 'id'),
                        "resolution_submitted_by_status": ITSMServices.triple_nested_data(data, 'resolution', 'submitted_on', 'status', ),
                        "resolution_resolution_attachments": ITSMServices.triple_nested_data(data, 'resolution', 'submitted_on',
                                                                                    'attachments'),
                        "resolution_content": ITSMServices.double_nested_data(data, 'resolution', 'content'),
                        "linked_to_request": data.get('linked_to_request', None),
                        "mode_name": ITSMServices.double_nested_data(data, 'mode', 'name'),
                        "mode_id": ITSMServices.double_nested_data(data, 'mode', 'id'),
                        "lifecycle": data.get('lifecycle', None),
                        "assets": data.get('assets', None),
                        "is_trashed": data.get('is_trashed', None),
                        "itsm_id": data.get('id', None),
                        "assigned_time_display_value": ITSMServices.double_nested_data(data, 'assigned_time', 'display_value'),
                        "assigned_time_value": ITSMServices.double_nested_data(data, 'assigned_time', 'value'),
                        "group_name": ITSMServices.double_nested_data(data, 'group', 'name'),
                        "group_id": ITSMServices.double_nested_data(data, 'group', 'id'),
                        "requester_email_id": ITSMServices.double_nested_data(data, 'requester', 'email_id'),
                        "requester_name": ITSMServices.double_nested_data(data, 'requester', 'name'),
                        "requester_mobile": ITSMServices.double_nested_data(data, 'requester', 'mobile'),
                        "requester_is_vipuser": ITSMServices.double_nested_data(data, 'requester', 'is_vipuser'),
                        "requester_id": ITSMServices.double_nested_data(data, 'requester', 'id'),
                        "requester_status": ITSMServices.double_nested_data(data, 'requester', 'status'),
                        "email_to": data.get('email_to', None),
                        "created_time_display_value": ITSMServices.double_nested_data(data, 'created_time', 'display_value'),
                        "created_time_value": ITSMServices.double_nested_data(data, 'created_time', 'value'),
                        "has_resolution_attachments": data.get('has_resolution_attachments'),
                        "approval_status": data.get('approval_status'),
                        "impact_name": ITSMServices.double_nested_data(data, 'impact', 'name'),
                        "impact_id": ITSMServices.double_nested_data(data, 'impact', 'id'),
                        "service_category_name": ITSMServices.double_nested_data(data, 'service_category', 'name'),
                        "service_category_id": ITSMServices.double_nested_data(data, 'service_category', 'id'),
                        "sla_name": ITSMServices.double_nested_data(data, 'sla', 'name'),
                        "sla_id": ITSMServices.double_nested_data(data, 'sla', 'id'),
                        "resolved_time_display_value": ITSMServices.double_nested_data(data, 'resolved_time', 'display_value'),
                        "resolved_time_value": ITSMServices.double_nested_data(data, 'resolved_time', 'value'),
                        "priority_color": ITSMServices.double_nested_data(data, 'priority', 'color'),
                        "priority_name": ITSMServices.double_nested_data(data, 'priority', 'name'),
                        "priority_id": ITSMServices.double_nested_data(data, 'priority', 'id'),
                        "created_by_email_id": ITSMServices.double_nested_data(data, 'created_by', 'email_id'),
                        "created_by_name": ITSMServices.double_nested_data(data, 'created_by', 'name'),
                        "created_by_mobile": ITSMServices.double_nested_data(data, 'created_by', 'mobile'),
                        "created_by_is_vipuser": ITSMServices.double_nested_data(data, 'created_by', 'is_vipuser'),
                        "created_by_id": ITSMServices.double_nested_data(data, 'created_by', 'id'),
                        "created_by_status": ITSMServices.double_nested_data(data, 'created_by', 'status'),
                        "last_updated_time_display_value": ITSMServices.double_nested_data(data, 'last_updated_time', 'display_value'),
                        "last_updated_time_value": ITSMServices.double_nested_data(data, 'last_updated_time', 'value'),
                        "has_notes": data.get('has_notes'),
                        "udf_fields_udf_sline_4501": ITSMServices.double_nested_data(data, 'udf_fields', 'udf_sline_4501'),
                        "udf_fields_udf_long_4502": ITSMServices.double_nested_data(data, 'udf_fields', 'udf_long_4502'),
                        "impact_details": data.get('impact_details', None),
                        "subcategory_name": ITSMServices.double_nested_data(data, 'subcategory', 'name'),
                        "subcategory_id": ITSMServices.double_nested_data(data, 'subcategory', 'id'),
                        "email_cc": data.get('email_cc', None),
                        "status_color": ITSMServices.double_nested_data(data, 'status', 'color'),
                        "status_name": ITSMServices.double_nested_data(data, 'status', 'name'),
                        "status_id": ITSMServices.double_nested_data(data, 'status', 'id'),
                        "template_name": ITSMServices.double_nested_data(data, 'template', 'name'),
                        "template_id": ITSMServices.double_nested_data(data, 'template', 'id'),
                        "email_ids_to_notify": data.get('email_ids_to_notify'),
                        "request_type_name": ITSMServices.double_nested_data(data, 'request_type', 'name'),
                        "request_type_id": ITSMServices.double_nested_data(data, 'request_type', 'id'),
                        "is_request_contract_applicable": data.get('is_request_contract_applicable', None),
                        "time_elapsed_display_value": ITSMServices.double_nested_data(data, 'time_elapsed', 'display_value'),
                        "time_elapsed_value": ITSMServices.double_nested_data(data, 'time_elapsed', 'value'),
                        "description": data.get('description', None),
                        "has_dependency": data.get('has_dependency', None),
                        "closure_info_requester_ack_comments": ITSMServices.double_nested_data(data, 'closure_info', 'requester_ack_comments'),
                        "closure_info_closure_code": ITSMServices.double_nested_data(data, 'closure_info', 'closure_code'),
                        "closure_info_closure_comments": ITSMServices.double_nested_data(data, 'closure_info', 'closure_comments'),
                        "closure_info_signoff": ITSMServices.double_nested_data(data, 'closure_info', 'signoff'),
                        "closure_info_requester_ack_resolution": ITSMServices.double_nested_data(data, 'closure_info', 'requester_ack_resolution'),
                        "has_conversation": data.get('has_conversation', None),
                        "callback_url": data.get('callback_url', None),
                        "is_service_request": data.get('is_service_request', None),
                        "urgency_name": ITSMServices.double_nested_data(data, 'urgency', 'name'),
                        "urgency_id": data.get('urgency', 'id'),
                        "is_shared": data.get('is_shared', None),
                        "billing_status_billingstatusid": ITSMServices.double_nested_data(data, 'billing_status', 'billingstatusid'),
                        "billing_status_billingstatusname": ITSMServices.double_nested_data(data, 'billing_status', 'billingstatusname'),
                        "accountcontract_serviceplan_id": ITSMServices.triple_nested_data(data, 'accountcontract', 'serviceplan', 'id'),
                        "accountcontract_isactivecontract": ITSMServices.double_nested_data(data, 'accountcontract', 'isactivecontract'),
                        "accountcontract_contractnumber": ITSMServices.double_nested_data(data, 'accountcontract', 'contractnumber'),
                        "accountcontract_contractid": ITSMServices.double_nested_data(data, 'accountcontract', 'contractid'),
                        "accountcontract_contractname": ITSMServices.double_nested_data(data, 'accountcontract', 'contractname'),
                        "accountcontract_description": ITSMServices.double_nested_data(data, 'accountcontract', 'description'),
                        "accountcontract_billunclosed": ITSMServices.double_nested_data(data, 'accountcontract', 'billunclosed'),
                        "has_request_initiated_change": data.get('has_request_initiated_change'),
                        "request_template_task_ids": data.get('request_template_task_ids'),
                        "department_name": ITSMServices.double_nested_data(data, 'department', 'name'),
                        "department_id": ITSMServices.double_nested_data(data, 'department', 'id'),
                        "is_reopened": data.get('is_reopened', None),
                        "has_draft": data.get('has_draft', None),
                        "has_attachments": data.get('has_attachments', None),
                        "has_linked_requests": data.get('has_linked_requests', None),
                        "is_overdue": data.get('is_overdue', None),
                        "technician_email_id": ITSMServices.double_nested_data(data, 'technician', 'email_id'),
                        "technician_name": ITSMServices.double_nested_data(data, 'technician', 'name'),
                        "technician_mobile": ITSMServices.double_nested_data(data, 'technician', 'mobile'),
                        "technician_id": ITSMServices.double_nested_data(data, 'technician', 'id'),
                        "technician_status": ITSMServices.double_nested_data(data, 'technician', 'status'),
                        "is_billable": data.get('is_billable', None),
                        "has_problem": data.get('has_problem', None),
                        "due_by_time": data.get('due_by_time', None),
                        "is_fcr": data.get('is_fcr', None),
                        "has_project": data.get('has_project', None),
                        "site_name": ITSMServices.double_nested_data(data, 'site', 'name'),
                        "site_id": ITSMServices.double_nested_data(data, 'site', 'id'),
                        "completed_time_display_value": ITSMServices.double_nested_data(data, 'completed_time', 'display_value'),
                        "completed_time_value": ITSMServices.double_nested_data(data, 'completed_time', 'value'),
                        "category_name": ITSMServices.double_nested_data(data, 'category', 'name'),
                        "category_id": ITSMServices.double_nested_data(data, 'category', 'id'),
                        "account_name": ITSMServices.double_nested_data(data, 'account', 'name'),
                        "account_id": ITSMServices.double_nested_data(data, 'account', 'id'),
                        "subcategory": data.get('subcategory', None),
                        "closure_info_closure_code_name": ITSMServices.double_nested_data(data, 'closure_info', 'closure_code_name'),
                        "closure_info_closure_code_id": ITSMServices.double_nested_data(data, 'closure_info', 'closure_code_id'),
                        "mode": data.get('mode', None),
                        "item": data.get('item', None),
                        "level_name": ITSMServices.double_nested_data(data, 'level', 'name'),
                        "level_id": ITSMServices.double_nested_data(data, 'level', 'id'),
                        "udf_fields_udf_sline_5401": ITSMServices.double_nested_data(data, 'udf_fields', 'udf_sline_5401'),
                        "udf_fields_udf_long_3302": ITSMServices.double_nested_data(data, 'udf_fields', 'udf_long_3302'),
                        "subject": data.get('subject', None)
                    }
                    # values is defined to create objects in itsm extractor table
                    values = EXTRACTOR_ITSM.objects.update_or_create(defaults=itsm, itsm_id=data.get("id"))
            end_time = datetime.datetime.now()
            status = "Success"
            return a
        except Exception as e:
            end_time = datetime.datetime.now()
            status = "Failed"
            return e
        finally:
            audit_dict = {
                "start_date": start_time,
                "end_date": end_time,
                "status": status
            }
            audit = Audit_ITSM_EXTRACTOR.objects.create(**audit_dict)
            return audit_dict
