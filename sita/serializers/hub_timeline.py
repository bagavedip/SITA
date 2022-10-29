from sita.constants.filter_map import Map


class HubTimeline:
    """
     Serializer for insights Timeline view
    """
    def __init__(self, request) -> None:
        self.request_filters = []
        self.header_filters = []
        self.model_group_map = []
        self.queryset = None
        self.datasets = []
        self.hier_data = {}
        self.legend_filter = ""
        filter_data = request.data
        self.start_date = filter_data.get('fromDate')
        self.end_date = filter_data.get('toDate')
        self.request_filters.append((filter_data.get('filterOptions').get('headerOption')))
        filters = filter_data.get('filterOptions').get('headerFilters')
        for filters in filters:
            self.header_filters.append(filters)
        for group in self.request_filters:
            self.model_group_map = self.model_group_map + Map.get_filter(group).split(',')
