from sita.constants import oei_constants


class TicketDetailsSerializer:
    """
     Serializer for Ticket details OEI(ITSM)
    """

    def __init__(self, request) -> None:

        request_data = request.data

        self.start_date = request_data.get('fromDate')
        self.end_date = request_data.get('toDate')
        region = request_data.get('region')
        self.filters = {}
        self.filters['CreatedTime__gte'] = self.start_date
        self.filters['Ending_time__lte'] = self.end_date
        filter_arr = region.split("*")
        for filter_str in filter_arr:
            filter = filter_str.split("*")[0].split("~")[0]
            filter_key_val = filter.split("=")
            if request_data.get("selectedOption") == 'Tickets':
                for childfilters in request_data.get("selectedFilter"):
                    if childfilters == 'First_Response_Time':
                        self.filters[filter_key_val[0]] = filter_key_val[1]
                    elif childfilters == "Response_Time":
                        self.filters[filter_key_val[0]] = filter_key_val[1]
                    else:
                        self.filters[filter_key_val[0]] = filter_key_val[1].split('-')[0]
            else:
                self.filters[filter_key_val[0]] = filter_key_val[1]
                
        self.columns_headers = []
        self.select_cols = []
        for key in oei_constants.INSIGHT_TABLE_HEADER.keys():
            self.select_cols.append(oei_constants.INSIGHT_TABLE_HEADER.get(key))
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
            col_headers.append(col)

        grid_data = []
        for row in data:
            row_data = {}
            newstring = ''
            for index in range(len(row)):
                if len(str(row.get(self.select_cols[index])).split()) > 10:
                    details = list(str(row.get(self.select_cols[index])).split())
                    for i in range(15):
                        newstring = newstring + " " + details[i]
                    row_data["column" + (str(index + 1))] = newstring + "..."
                else: 
                    row_data["column" + (str(index + 1))] = str(row.get(self.select_cols[index]))
            grid_data.append(row_data)

        response_json = {
            "gridSelectedFilter": {
                "startDate": self.start_date,
                "endDate": self.end_date,
                "selectedDropdownFiters": []
            },
            "gridAddOn": {
                "showFirstColumnAsCheckbox": True,
                "showLastColumnAsAction": True
            },
            "gridHeader": col_headers,
            "gridData": grid_data

        }
        return response_json
