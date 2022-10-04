class Dataset:
    """
     Dataset class is used to show response
     of insights chart_data in listed format.
    """

    def init_response_dataset(self):
        dataset = {
            "id": 0,
            "label": "",
            "showDatalabel": False,
            "dataLabelColor": "",
            "data": [],
            "originalData": [],
            "hierarchy": [],
            "backgroundColor": [],
            "labels": [],
            "spacing": 45,
            "weight": 5
        }
        return dataset
    
    def _get_dict(self, key):
        return {
            "key": key,
            "label": "",
            "incident_count": 0
        }

    def get_hierarchy_dict(self, level):
        hierarchy_dict = None
        if level == 1:
            hierarchy_dict = self._get_dict(1)
        elif level == 2:
            hierarchy_dict = self._get_dict(1)
            hierarchy_dict['child'] = self._get_dict(2)
        elif level == 3:
            hierarchy_dict = self._get_dict(1)
            hierarchy_dict_2 = self._get_dict(2)
            hierarchy_dict_2['child'] = self._get_dict(3)
            hierarchy_dict['child'] = hierarchy_dict_2
        else:
            hierarchy_dict = self._get_dict(1)
            hierarchy_dict_2 = self._get_dict(2)
            hierarchy_dict_3 = self._get_dict(3)
            hierarchy_dict_3['child'] = self._get_dict(4)
            hierarchy_dict_2['child'] = hierarchy_dict_3
            hierarchy_dict['child'] = hierarchy_dict_2
        return hierarchy_dict

