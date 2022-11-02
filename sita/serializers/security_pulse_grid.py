from sita.constants import security_pulse_constants

from sita.models.security_pulse import SecurityPulse

class SecurityPulseGridSerializer:
    """
     Serializer for Ticket Details for Insights(Hub)
    """

    def __init__(self, request) -> None:

        request_data = request.data

        self.columns_headers = []
        self.select_cols = []
        for key in security_pulse_constants.SECURITY_PULSE_TABLE_HEADER.keys():
            self.select_cols.append(security_pulse_constants.SECURITY_PULSE_TABLE_HEADER.get(key))
            self.columns_headers.append(key)

    def get_response(self, data):
        col_headers = []
        for index in range(len(self.columns_headers)):
            col = {
                "key": "column" + str(index + 1),
                "headerText": self.columns_headers[index],
                "isSorting": True,
                "type": "TEXT"
            }
            col.update({"hideOnUI": True}) if index == 0 else col.update({"hideOnUI": False})
            col_headers.append(col)

        grid_data = []
        for row in data:
            row_data = {}
            None if row.get("selected_assets") is None else row.update({"selected_assets": ", ".join(row.get("selected_assets"))})
            None if row.get("updated_at") is None else row.update({"updated_at": row.get("updated_at").strftime("%m-%d-%Y")})
            row.update({"is_published": "Publish"}) if row.get("is_published") else row.update({"is_published": "Draft"})
            a = row.get("created_by")
            number = row.get("id")
            queryset = SecurityPulse.objects.get(id=number)
            created = queryset.created_by.first_name + " " + queryset.created_by.last_name
            for index in range(len(row)):
                row_data["column" + (str(index + 1))] = str(row.get(self.select_cols[index]))
                None if row.get("created_by") is None else row.update({"created_by": created})
            grid_data.append(row_data)

        response_json = {
            "gridAddOn": {
                "showFirstColumnAsCheckbox": False,
                "showLastColumnAsAction": True
            },
            "gridHeader": col_headers,
            "gridData": grid_data

        }
        return response_json
