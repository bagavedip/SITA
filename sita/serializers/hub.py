from sita.constants.filter_map import Map
from sita.constants.dataset import Dataset
from sita.constants.color import ColorMap


class InsightsSerializer:
    """
     Serializer for Insights(Hub) models
    """
    def __init__(self, request) -> None:
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
        filterOptions = filter_data.get('filterOptions').get('headerFilters')
        add_criticality = False
        for filter in filterOptions:
            if filter == 'Criticality':
                add_criticality = True
            else:
                self.request_filters.append(filter)
        self.request_filters.append(filter_data.get('filterOptions').get('headerOption'))
        temp_request_filters = []
        for option in Map.get_master():
            if option in self.request_filters:
                temp_request_filters.append(option)
        self.request_filters = temp_request_filters
        header_option = filter_data.get('filterOptions').get('headerOption')
        filters = Map.get_filter(header_option).split(",")
        if len(filters) > 1:
            self.legend_filter = filters[1]
        else:
            self.legend_filter = filters[0]
        if add_criticality:
            self.request_filters.append('Criticality')
        self.depth = len(self.request_filters)
        index = 1
        for filter in self.request_filters:
            self.model_group_map = self.model_group_map + Map.get_filter(filter).split(',')
            ds = Dataset().init_response_dataset()
            ds['id'] = index
            ds['label'] = filter
            self.datasets.append(ds)
            index += 1

    def insert_children(self, start_index, data_dict, data, events):
        for index in range(start_index, len(self.request_filters)):
            key = self.request_filters[index]
            val = {
                "name": data[index],
                "events": events
            }
            if key in data_dict.keys():
                obj_arr = data_dict.get(key)
                data_dict["events"] = data_dict["events"] + events
                obj_arr.append(val)
            else:
                data_dict[key] = [val]
            self.insert_children(index + 1, val, data, events)
            break

    def update_children(self, start_index, data_dict, data, events):
        for index in range(start_index, len(self.request_filters)):
            key = self.request_filters[index]
            if key in data_dict.keys():
                obj_arr = data_dict.get(key)
                for item in obj_arr:
                    if item["name"] == data[index]:
                        data_dict["events"] = data_dict["events"] + events
                        self.update_children(index + 1, item, data, events)
                        break
                else:
                    val = {
                        "name": data[index],
                        "events": events
                    }
                    data_dict["events"] = data_dict["events"] + events
                    obj_arr.append(val)
                    self.insert_children(index + 1, val, data, events)
                    break
                break
            else:
                val = {
                    "name": data[index],
                    "events": events
                }
                self.hier_data[key] = [val]
                self.insert_children(index + 1, val, data, events)
            break

    def update_hierarcy_data(self, data, events):
        for index in range(len(self.request_filters)):
            key = self.request_filters[index]
            if key in self.hier_data.keys():
                obj_arr = self.hier_data.get(key)
                for item in obj_arr:
                    if item["name"] == data[index]:
                        self.update_children(index + 1, item, data, events)
                        break
                else:
                    val = {
                        "name": data[index],
                        "events": events
                    }
                    obj_arr.append(val)
                    self.insert_children(index + 1, val, data, events)
                    break
                break
            else:
                val = {
                    "name": data[index],
                    "events": events
                }
                self.hier_data[key] = [val]
                self.insert_children(index + 1, val, data, events)
            break

    def build_dataset_level1(self):
        data = []
        originalData = []
        hierarchy = []
        labels = []
        backgroundColor = []
        dataLabelColor = ""
        if self.hier_data.get(self.datasets[0]['label']) is not None:
            for item in self.hier_data.get(self.datasets[0]['label']):
                data.append(item['events'])
                originalData.append(item['events'])
                lable_name = self.datasets[0]['label']
                columns = Map.get_filter(lable_name)
                id_col = columns.split(",")[0]
                hierarchy.append(id_col + "=" + item['name'] + "~" + str(item['events']))
                labels.append(item['name'])
                id = item['name']
                if '-' in item['name']:
                    id = item['name'].split("-")[0]
                backgroundColor.append(ColorMap.get_color(self.datasets[0]['label'], id))
                dataLabelColor = ColorMap.get_color(self.datasets[0]['label'],id)
        self.datasets[0]['data'] = data
        self.datasets[0]['originalData'] = originalData
        self.datasets[0]['hierarchy'] = hierarchy
        self.datasets[0]['labels'] = labels
        self.datasets[0]['backgroundColor'] = backgroundColor
        self.datasets[0]['dataLabelColor'] = dataLabelColor

    def build_dataset_level2(self):
        data = []
        originalData = []
        hierarchy = []
        labels = []
        backgroundColor = []
        dataLabelColor = ""
        if self.hier_data.get(self.datasets[0]['label']) is not None:
            for item in self.hier_data.get(self.datasets[0]['label']):
                lable_name = self.datasets[0]['label']
                columns = Map.get_filter(lable_name)
                id_col = columns.split(",")[0]
                parent_hierarchy = id_col + "=" + item['name'] + "~" + str(item['events'])
                for child_item in item.get(self.datasets[1]['label']):
                    data.append(child_item['events'])
                    originalData.append(child_item['events'])
                    lable_name = self.datasets[1]['label']
                    columns = Map.get_filter(lable_name)
                    id_col = columns.split(",")[0]
                    hierarchy.append(
                        parent_hierarchy + "*" + id_col + "=" + child_item['name'] + "~" + str(child_item['events']))
                    labels.append(child_item['name'])
                    id = child_item['name']
                    if '-' in child_item['name']:
                        id = child_item['name'].split("-")[0]
                    backgroundColor.append(ColorMap.get_color(self.datasets[1]['label'], id))
                    dataLabelColor = ColorMap.get_color(self.datasets[1]['label'],id)
        self.datasets[1]['data'] = data
        self.datasets[1]['originalData'] = originalData
        self.datasets[1]['hierarchy'] = hierarchy
        self.datasets[1]['labels'] = labels
        self.datasets[1]['backgroundColor'] = backgroundColor
        self.datasets[1]['dataLabelColor'] = dataLabelColor
        self.datasets[1]['spacing'] = 30
        self.datasets[1]['weight'] = 8

    def build_dataset_level3(self):
        data = []
        originalData = []
        hierarchy = []
        labels = []
        backgroundColor = []
        dataLabelColor = ""
        if self.hier_data.get(self.datasets[0]['label']) is not None:
            for item in self.hier_data.get(self.datasets[0]['label']):
                lable_name = self.datasets[0]['label']
                columns = Map.get_filter(lable_name)
                id_col = columns.split(",")[0]
                parent_hierarchy = id_col + "=" + item['name'] + "~" + str(item['events'])
                for child_item in item.get(self.datasets[1]['label']):
                    lable_name = self.datasets[1]['label']
                    columns = Map.get_filter(lable_name)
                    id_col = columns.split(",")[0]
                    parent2_hierarchy = parent_hierarchy + "*" + id_col + "=" + child_item['name'] + "~" + str(
                        child_item['events'])
                    for child2_item in child_item.get(self.datasets[2]['label']):
                        data.append(child2_item['events'])
                        originalData.append(child2_item['events'])
                        lable_name = self.datasets[2]['label']
                        columns = Map.get_filter(lable_name)
                        id_col = columns.split(",")[0]
                        hierarchy.append(parent2_hierarchy + "*" + id_col + "=" + child2_item['name'] + "~" + str(
                            child2_item['events']))
                        labels.append(child2_item['name'])
                        id = child2_item['name']
                        if '-' in child2_item['name']:
                            id = child2_item['name'].split("-")[0]
                        backgroundColor.append(ColorMap.get_color(self.datasets[2]['label'], id))
                        dataLabelColor = ColorMap.get_color(self.datasets[2]['label'],id)
        self.datasets[2]['data'] = data
        self.datasets[2]['originalData'] = originalData
        self.datasets[2]['hierarchy'] = hierarchy
        self.datasets[2]['labels'] = labels
        self.datasets[2]['backgroundColor'] = backgroundColor
        self.datasets[2]['dataLabelColor'] = dataLabelColor
        self.datasets[2]['spacing'] = 15
        self.datasets[2]['weight'] = 2

    def build_dataset_level4(self):
        data = []
        originalData = []
        hierarchy = []
        labels = []
        backgroundColor = []
        dataLabelColor = ""
        if self.hier_data.get(self.datasets[0]['label']) is not None:
            for item in self.hier_data.get(self.datasets[0]['label']):
                lable_name = self.datasets[0]['label']
                columns = Map.get_filter(lable_name)
                id_col = columns.split(",")[0]
                parent_hierarchy = id_col + "=" + item['name'] + "~" + str(item['events'])
                for child_item in item.get(self.datasets[1]['label']):
                    lable_name = self.datasets[1]['label']
                    columns = Map.get_filter(lable_name)
                    id_col = columns.split(",")[0]
                    parent2_hierarchy = parent_hierarchy + "*" + id_col + "=" + child_item['name'] + "~" + str(
                        child_item['events'])
                    for child2_item in child_item.get(self.datasets[2]['label']):
                        lable_name = self.datasets[2]['label']
                        columns = Map.get_filter(lable_name)
                        id_col = columns.split(",")[0]
                        parent3_hierarchy = parent2_hierarchy + "*" + id_col + "=" + child2_item['name'] + "~" + str(
                            child2_item['events'])
                        for child3_item in child2_item.get(self.datasets[3]['label']):
                            data.append(child3_item['events'])
                            originalData.append(child3_item['events'])
                            lable_name = self.datasets[3]['label']
                            columns = Map.get_filter(lable_name)
                            id_col = columns.split(",")[0]
                            hierarchy.append(parent3_hierarchy + "*" + id_col + "=" + child3_item['name'] + "~" + str(
                                child3_item['events']))
                            labels.append(child3_item['name'])
                            id = child3_item['name']
                            if '-' in child3_item['name']:
                                id = child2_item['name'].split("-")[0]
                            backgroundColor.append(ColorMap.get_color(self.datasets[3]['label'], id))
                            dataLabelColor = ColorMap.get_color(self.datasets[3]['label'],id)
        self.datasets[3]['data'] = data
        self.datasets[3]['originalData'] = originalData
        self.datasets[3]['hierarchy'] = hierarchy
        self.datasets[3]['labels'] = labels
        self.datasets[3]['backgroundColor'] = backgroundColor
        self.datasets[3]['dataLabelColor'] = dataLabelColor
        self.datasets[3]['spacing'] = 15
        self.datasets[3]['weight'] = 2

    def build_dataset(self):
        self.build_dataset_level1()
        if len(self.datasets) == 2:
            self.build_dataset_level2()
        elif len(self.datasets) == 3:
            self.build_dataset_level2()
            self.build_dataset_level3()
        else:
            self.build_dataset_level2()
            self.build_dataset_level3()
            self.build_dataset_level4()
        temp_datasets = []
        for dataaet in reversed(self.datasets):
            temp_datasets.append(dataaet)
        self.datasets = temp_datasets

    def set_requst_queryset(self, obj):
        self.queryset = obj
        for row in obj:
            filter_vals = []
            for filter in self.request_filters:
                col_data = ""
                for col_name in Map.get_filter(filter).split(','):
                    col_data = col_data + "-" + row.get(col_name) if row.get(col_name) else ""
                col_data = col_data[1:]
                temp_label = col_data
                filter_vals.append(temp_label)
            self.update_hierarcy_data(filter_vals, row.get('events'))
        self.build_dataset()
