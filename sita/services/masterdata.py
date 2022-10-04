from sita.serializers.masterdata import MasterDataSerialiser
from sita.models.fact_insights import FACT_INSIGHTS


class MasterDataService:

    @staticmethod
    def get_master_data(response_obj: MasterDataSerialiser):
        master_data = []
        for master_label in response_obj.table_columns:
            select_cols = master_label.split(",")
            query_data = FACT_INSIGHTS.objects.values(*select_cols).distinct()
            master = []
            for row in query_data:
                rec = {}
                for col in select_cols:
                    rec[col] = row.get(col)
                master.append(rec)
            master_data.append(master)
        response_obj.master_data = master_data
