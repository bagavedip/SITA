import requests

from sita.models.extractor_itsm import EXTRACTOR_ITSM


class ITSMServices:
    @staticmethod
    def r(data, key1, key2):
        return data.get(key1, {}).get(key2) if data.get(key1) is not None else None

    @staticmethod
    def itsm_data(data, key1, key2, key3):
        return data.get(key1, {}).get(key2, {}).get(key3) if data.get(key1) is not None else None

    @staticmethod
    def itsm_dump():
        url = 'https://192.168.201.20/api/v3/requests'
        headers = {"technician_key": "DCFFE887-4B30-4E7E-9608-6379B483414E"}
        response = requests.get(url, headers=headers, verify=False)
        data = response.json().get('requests')
        numbers = []
        a = []
        for keys in data:
            num = keys.get('id')
            query = EXTRACTOR_ITSM.objects.update(itsm_id=num)
            numbers.append(num)
            for n in numbers:
                url = "https://192.168.201.20/api/v3/requests/" + str(n)
                headers = {"technician_key": "DCFFE887-4B30-4E7E-9608-6379B483414E"}
                response = requests.get(url, headers=headers, verify=False)
                data = response.json().get('request')
                itsm = {
                    "resolution_submitted_on_display_value": ITSMServices.itsm_data(data, 'resolution', 'submitted_on',
                                                                                    'display_value'),
                    "resolution_submitted_on_value": ITSMServices.itsm_data(data, 'resolution', 'submitted_on', 'value'),
                    "resolution_submitted_by_email_id": ITSMServices.itsm_data(data, 'resolution', 'submitted_on', 'email_id'),
                    "resolution_submitted_by_name": ITSMServices.itsm_data(data, 'resolution', 'submitted_on', 'name'),
                    "resolution_submitted_by_mobile": ITSMServices.itsm_data(data, 'resolution', 'submitted_on', 'mobile'),
                    "resolution_submitted_by_is_vipuser": ITSMServices.itsm_data(data, 'resolution', 'submitted_on',
                                                                                 'is_vipuser'),
                    "resolution_submitted_by_id": ITSMServices.itsm_data(data, 'resolution', 'submitted_on', 'id'),
                    "resolution_submitted_by_status": ITSMServices.itsm_data(data, 'resolution', 'submitted_on', 'status', ),
                    "resolution_resolution_attachments": ITSMServices.itsm_data(data, 'resolution', 'submitted_on',
                                                                                'attachments'),
                    "resolution_content": ITSMServices.r(data, 'resolution', 'content'),
                    "linked_to_request": data.get('linked_to_request', None),
                    "mode_name": ITSMServices.r(data, 'mode', 'name'),
                    "mode_id": ITSMServices.r(data, 'mode', 'id'),
                    "lifecycle": data.get('lifecycle', None),
                    "assets": data.get('assets', None),
                    "is_trashed": data.get('is_trashed', None),
                    "itsm_id": data.get('id', None),
                    "assigned_time_display_value": ITSMServices.r(data, 'assigned_time', 'display_value'),
                    "assigned_time_value": ITSMServices.r(data, 'assigned_time', 'value'),
                    "group_name": ITSMServices.r(data, 'group', 'name'),
                    "group_id": ITSMServices.r(data, 'group', 'id'),
                    "requester_email_id": ITSMServices.r(data, 'requester', 'email_id'),
                    "requester_name": ITSMServices.r(data, 'requester', 'name'),
                    "requester_mobile": ITSMServices.r(data, 'requester', 'mobile'),
                    "requester_is_vipuser": ITSMServices.r(data, 'requester', 'is_vipuser'),
                    "requester_id": ITSMServices.r(data, 'requester', 'id'),
                    "requester_status": ITSMServices.r(data, 'requester', 'status'),
                    "email_to": data.get('email_to', None),
                    "created_time_display_value": ITSMServices.r(data, 'created_time', 'display_value'),
                    "created_time_value": ITSMServices.r(data, 'created_time', 'value'),
                    "has_resolution_attachments": data.get('has_resolution_attachments'),
                    "approval_status": data.get('approval_status'),
                    "impact_name": ITSMServices.r(data, 'impact', 'name'),
                    "impact_id": ITSMServices.r(data, 'impact', 'id'),
                    "service_category_name": ITSMServices.r(data, 'service_category', 'name'),
                    "service_category_id": ITSMServices.r(data, 'service_category', 'id'),
                    "sla_name": ITSMServices.r(data, 'sla', 'name'),
                    "sla_id": ITSMServices.r(data, 'sla', 'id'),
                    "resolved_time_display_value": ITSMServices.r(data, 'resolved_time', 'display_value'),
                    "resolved_time_value": ITSMServices.r(data, 'resolved_time', 'value'),
                    "priority_color": ITSMServices.r(data, 'priority', 'color'),
                    "priority_name": ITSMServices.r(data, 'priority', 'name'),
                    "priority_id": ITSMServices.r(data, 'priority', 'id'),
                    "created_by_email_id": ITSMServices.r(data, 'created_by', 'email_id'),
                    "created_by_name": ITSMServices.r(data, 'created_by', 'name'),
                    "created_by_mobile": ITSMServices.r(data, 'created_by', 'mobile'),
                    "created_by_is_vipuser": ITSMServices.r(data, 'created_by', 'is_vipuser'),
                    "created_by_id": ITSMServices.r(data, 'created_by', 'id'),
                    "created_by_status": ITSMServices.r(data, 'created_by', 'status'),
                    "last_updated_time_display_value": ITSMServices.r(data, 'last_updated_time', 'display_value'),
                    "last_updated_time_value": ITSMServices.r(data, 'last_updated_time', 'value'),
                    "has_notes": data.get('has_notes'),
                    "udf_fields_udf_sline_4501": ITSMServices.r(data, 'udf_fields', 'udf_sline_4501'),
                    "udf_fields_udf_long_4502": ITSMServices.r(data, 'udf_fields', 'udf_long_4502'),
                    "impact_details": data.get('impact_details', None),
                    "subcategory_name": ITSMServices.r(data, 'subcategory', 'name'),
                    "subcategory_id": ITSMServices.r(data, 'subcategory', 'id'),
                    "email_cc": data.get('email_cc', None),
                    "status_color": ITSMServices.r(data, 'status', 'color'),
                    "status_name": ITSMServices.r(data, 'status', 'name'),
                    "status_id": ITSMServices.r(data, 'status', 'id'),
                    "template_name": ITSMServices.r(data, 'template', 'name'),
                    "template_id": ITSMServices.r(data, 'template', 'id'),
                    "email_ids_to_notify": data.get('email_ids_to_notify'),
                    "request_type_name": ITSMServices.r(data, 'request_type', 'name'),
                    "request_type_id": ITSMServices.r(data, 'request_type', 'id'),
                    "is_request_contract_applicable": data.get('is_request_contract_applicable', None),
                    "time_elapsed_display_value": ITSMServices.r(data, 'time_elapsed', 'display_value'),
                    "time_elapsed_value": ITSMServices.r(data, 'time_elapsed', 'value'),
                    "description": data.get('description', None),
                    "has_dependency": data.get('has_dependency', None),
                    "closure_info_requester_ack_comments": ITSMServices.r(data, 'closure_info', 'requester_ack_comments'),
                    "closure_info_closure_code": ITSMServices.r(data, 'closure_info', 'closure_code'),
                    "closure_info_closure_comments": ITSMServices.r(data, 'closure_info', 'closure_comments'),
                    "closure_info_signoff": ITSMServices.r(data, 'closure_info', 'signoff'),
                    "closure_info_requester_ack_resolution": ITSMServices.r(data, 'closure_info', 'requester_ack_resolution'),
                    "has_conversation": data.get('has_conversation', None),
                    "callback_url": data.get('callback_url', None),
                    "is_service_request": data.get('is_service_request', None),
                    "urgency_name": ITSMServices.r(data, 'urgency', 'name'),
                    "urgency_id": data.get('urgency', 'id'),
                    "is_shared": data.get('is_shared', None),
                    "billing_status_billingstatusid": ITSMServices.r(data, 'billing_status', 'billingstatusid'),
                    "billing_status_billingstatusname": ITSMServices.r(data, 'billing_status', 'billingstatusname'),
                    "accountcontract_serviceplan_id": ITSMServices.itsm_data(data, 'accountcontract', 'serviceplan', 'id'),
                    "accountcontract_isactivecontract": ITSMServices.r(data, 'accountcontract', 'isactivecontract'),
                    "accountcontract_contractnumber": ITSMServices.r(data, 'accountcontract', 'contractnumber'),
                    "accountcontract_contractid": ITSMServices.r(data, 'accountcontract', 'contractid'),
                    "accountcontract_contractname": ITSMServices.r(data, 'accountcontract', 'contractname'),
                    "accountcontract_description": ITSMServices.r(data, 'accountcontract', 'description'),
                    "accountcontract_billunclosed": ITSMServices.r(data, 'accountcontract', 'billunclosed'),
                    "has_request_initiated_change": data.get('has_request_initiated_change'),
                    "request_template_task_ids": data.get('request_template_task_ids'),
                    "department_name": ITSMServices.r(data, 'department', 'name'),
                    "department_id": ITSMServices.r(data, 'department', 'id'),
                    "is_reopened": data.get('is_reopened', None),
                    "has_draft": data.get('has_draft', None),
                    "has_attachments": data.get('has_attachments', None),
                    "has_linked_requests": data.get('has_linked_requests', None),
                    "is_overdue": data.get('is_overdue', None),
                    "technician_email_id": ITSMServices.r(data, 'technician', 'email_id'),
                    "technician_name": ITSMServices.r(data, 'technician', 'name'),
                    "technician_mobile": ITSMServices.r(data, 'technician', 'mobile'),
                    "technician_id": ITSMServices.r(data, 'technician', 'id'),
                    "technician_status": ITSMServices.r(data, 'technician', 'status'),
                    "is_billable": data.get('is_billable', None),
                    "has_problem": data.get('has_problem', None),
                    "due_by_time": data.get('due_by_time', None),
                    "is_fcr": data.get('is_fcr', None),
                    "has_project": data.get('has_project', None),
                    "site_name": ITSMServices.r(data, 'site', 'name'),
                    "site_id": ITSMServices.r(data, 'site', 'id'),
                    "completed_time_display_value": ITSMServices.r(data, 'completed_time', 'display_value'),
                    "completed_time_value": ITSMServices.r(data, 'completed_time', 'value'),
                    "category_name": ITSMServices.r(data, 'category', 'name'),
                    "category_id": ITSMServices.r(data, 'category', 'id'),
                    "account_name": ITSMServices.r(data, 'account', 'name'),
                    "account_id": ITSMServices.r(data, 'account', 'id'),
                    "subcategory": data.get('subcategory', None),
                    "closure_info_closure_code_name": ITSMServices.r(data, 'closure_info', 'closure_code_name'),
                    "closure_info_closure_code_id": ITSMServices.r(data, 'closure_info', 'closure_code_id'),
                    "mode": data.get('mode', None),
                    "item": data.get('item', None),
                    "level_name": ITSMServices.r(data, 'level', 'name'),
                    "level_id": ITSMServices.r(data, 'level', 'id'),
                    "udf_fields_udf_sline_5401": ITSMServices.r(data, 'udf_fields', 'udf_sline_5401'),
                    "udf_fields_udf_long_3302": ITSMServices.r(data, 'udf_fields', 'udf_long_3302'),
                    "subject": data.get('subject', None)
                }
            values = EXTRACTOR_ITSM.objects.create(**itsm)
            a.append(itsm)
        return a
