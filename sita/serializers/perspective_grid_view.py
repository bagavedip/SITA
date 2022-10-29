from sita.constants import perspective_constants


class PerspectiveGridSerializer:
    """
     Serializer for Ticket Details for Insights(Hub)
    """

    def __init__(self, request) -> None:

        request_data = request.data

        self.start_date = request_data.get('fromDate')
        self.end_date = request_data.get('toDate')
        self.dropdownFilters = request_data.get("dropdownFilters")
        self.filters = {}
        self.filters['incident_start_date_time__gte'] = self.start_date
        self.filters['incident_end_date_time__lte'] = self.end_date

        self.columns_headers = []
        self.select_cols = []
        for key in perspective_constants.PERSPECTIVE_TABLE_HEADER.keys():
            self.select_cols.append(perspective_constants.PERSPECTIVE_TABLE_HEADER.get(key))
            self.columns_headers.append(key)

    def get_response(self, data):
        col_headers = []
        for index in range(len(self.columns_headers)):
            col = {
                "key": "column" + str(index + 1),
                "headerText": self.columns_headers[index],
                "isSorting": True,
                "type": "TEXT",
                "hideOnUI": False,
                "dataDisplayLength": 0,
            }
            col.update({"hideOnUI": True}) if index == 0 else col.update({"hideOnUI": False})
            col_headers.append(col)

        grid_data = []
        for row in data:
            row_data = {}
            None if row.get("created_at") is None else row.update({"created_at": row.get("created_at").strftime("%m-%d-%Y")})
            row.update({"is_published": "Publish"}) if row.get("is_published") else row.update({"is_published": "Draft"})
            for index in range(len(row)):
                row_data["column" + (str(index + 1))] = str(row.get(self.select_cols[index]))
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
