filter_map = {
    "SLA": "sla_name",
    "Priority": "Priority",
    "Category": "category_id,service_category",
    "First_Response_Time": "response_time",
    "Response_Time": "resolved_time",
    "False_Positives": "RequestType",
    "Reopened": "reopened",
    "Status": "RequestStatus",
    "value0": "is_overdue",
    "value1": "is_overdue",
    "value2": "is_overdue",
    "value3": "is_overdue",
    "Tickets": "Itsm_id"
}


class Map:
    """
     map class is used to map column in models
     according to request in serializer of OEI.
    """
    @staticmethod
    def get_filter(name):
        return filter_map.get(name)
