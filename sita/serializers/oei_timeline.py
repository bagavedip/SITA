from sita.constants.oei_filters import Map


class OeiTimeline:
    """
     Serializer is used for OEI(ITSM) timeline view
    """
    def __init__(self, request) -> None:
        self.header_filters = []
        self.request_filters = []
        self.model_group_map = []
        self.queryset = None
        self.datasets = []
        self.hier_data = {}
        self.donut_center = {}
        self.legend_filter = ""
        filter_data = request.data
        self.start_date = filter_data.get('fromDate')
        self.end_date = filter_data.get('toDate')
        self.request_filters.append((filter_data.get('filterOptions').get('headerOption')))
        filters = filter_data.get('filterOptions').get('headerFilters')
        for filter in filters:
            self.header_filters.append(filter)
        for filter in self.request_filters:
            self.model_group_map = self.model_group_map + Map.get_filter(filter).split(',')
            
