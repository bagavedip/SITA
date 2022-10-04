class MasterDataSerialiser:
    """
    Serializer for Dropdown Data of Insights.
    """

    def __init__(self):
        self.drop_down_ids = ["Asset Type", "Geography", "ORG"]
        self.table_columns = ["asset_type", "location_id,location_name", "entity_id,entity_name"]
        self.master_data = []
    
    def get_response(self):
        if len(self.master_data) == 0:
            return []
        
        response = []

        # for index in range(len(self.drop_down_ids)):
        #     item = {}
        #     item['id'] = self.drop_down_ids[index]
        #     dropdownoptions = []
        #     dropdown_item = self.master_data[index]
        #     for dropdown_data in dropdown_item:
        #         dropdown_values = {}
        #         dropdown_values[]


class OeiMasterDataSerialiser:
    """
    Serializer for Dropdown Data of OEI.
    """

    def __init__(self):
        self.drop_down_ids = ["Priority", "Category", "Reopened %", "Service", "First response Time", "Status"]
        self.table_columns = ["ServiceCategory", "Priority", "Reopened"]
        self.master_data = []

    def get_response(self):
        if len(self.master_data) == 0:
            return []

        response = []
