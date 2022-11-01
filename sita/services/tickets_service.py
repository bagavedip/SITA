from sita.models.fact_insights import FACT_INSIGHTS
from django.db.models import Q
from sita.serializers.ticket_details import TicketDetailsSerializer


class TicketsService:
    """
     Service for Ticket Details of hub(insights) models
    """

    @staticmethod
    def get_tickets(response_obj: TicketDetailsSerializer):
        """
        Function for getting ticket details 
        """
        filter_q = Q(**response_obj.filters)
        query_data = FACT_INSIGHTS.objects.filter(filter_q).values(*response_obj.select_cols)
        return query_data
