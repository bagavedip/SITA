import calendar
import logging
from datetime import timedelta, datetime

from dateutil import relativedelta
from django.db.models import Count, Q

from sita.models.add_oei_comment import AddOeiComment
from sita.models.fact_oei import FACT_OEI
from sita.models.insights_update import HubUpdate
from sita.serializers.oei_timeline import OeiTimeline
from sita.serializers.oei_serializers import OeiSerializer
from sita.serializers.oei_ticket_details import TicketDetailsSerializer

logger = logging.getLogger(__name__)


class ITSMService:
    """
     Services for ITSM Models
    """
    
    @staticmethod
    def get_queryset():
        """Function to return all ITSM data"""
        return FACT_OEI.objects.all()

    @staticmethod
    def itsm_filter(asset):
        """
         Function to return filter asset name
        """

        filtered_data = ITSMService.get_queryset().filter(Asset_Name=asset)
        return filtered_data

    @staticmethod
    def get_oei(response_obj: OeiSerializer):
        """
        Function for Oei donut chart
        """
        query_data = (
            FACT_OEI.objects.filter(CreatedTime__gte=response_obj.start_date,
                                    Ending_time__lte=response_obj.end_date).values(*response_obj.model_group_map)
            .order_by().annotate(events=Count('Itsm_id'))
        )
        response_obj.set_request_queryset(query_data)
        return query_data

    @staticmethod
    def get_tickets(response_obj: TicketDetailsSerializer):
        """
        Function for Oei Ticket details information.
        """
        filter_q = Q(**response_obj.filters)
        query_data = FACT_OEI.objects.filter(filter_q).values(*response_obj.select_cols)
        return query_data

    @staticmethod
    def asset_details(ticket):
        """
         Functions for details page of OEI tickets
        """
        data = ITSMService.get_queryset().filter(SIEM_id=ticket)
        updates = HubUpdate.objects.all().filter(soar_id=ticket).order_by('-update_date')[:6]
        assets = str(data.count())
        asset_names = []
        request_status = {}
        card = []
        incident_details = {}
        resolution_status = {}
        other_details = {}
        for query in data:
            asset_names.append(query.Asset_Name)
            request_status = {"text": query.Subject + " " + query.SIEM_id, "color": "#ffc107"}
            time_to_close = (query.assigned_time - query.CreatedTime)
            time = int(abs(time_to_close).total_seconds() / 3600)
            time_to_close = {"cardTitle": str(time) + " Hrs", "textColor": "#ffc107", "cardSubTitle": "Time to close",
                             "cardIcon": "OrangeWait"}
            a = query.CreatedTime
            b = query.sla_completion_time
            if b:
                c = a + timedelta(days=int(b))
            else:
                c = a
                
            expected_closure = (c - query.CreatedTime)
            time = int(abs(expected_closure).total_seconds() / 3600)
            expected_closure = {"cardTitle": str(time) + " Hrs", "textColor": "#ffc107",
                                "cardSubTitle": "Expected closure", "cardIcon": "BlueChartLineUp"}
            if query.Priority == "2. Alta":
                priority = "RED"
                color = "#ff0000"
                card_icon = "RedCaution"
            elif query.Priority == "4. Baja":
                priority = "Green"
                color = "#00FF00"
                card_icon = "GreenCaution"
            else:
                priority = "Orange"
                color = "#FFA500"
                card_icon = "OrangeCaution"
            tread_level = {"cardTitle": priority, "textColor": color, "cardSubTitle": "Threat Level",
                           "cardIcon": card_icon}
            card = [tread_level, time_to_close, expected_closure]
            incident_details = {"title": "TICKET DETAILS",
                                "description": "ITSM Case:" + query.Itsm_id + "\n SOAR ID: " + query.SOAR_ID}
            resolution_status = {
                "title": "RESOLUTION STATUS",
                "resolutionDetails": {
                    "title": "Resolution Details",
                    "description": query.Resolution,
                    "isEditable": "true"
                },
                "resolutionOwner": {

                    "title": "Resolution Owner",
                    "description": query.submitted_by,
                    "isEditable": "true"
                }
            }
        assets_name = assets + ":" + str(asset_names)
        details = [{
            "subTitle": "Assets Affected",
            "value": assets_name,
            "valueColor": "#333333"
        },
            {
                "subTitle": "Assets Type",
                "value": query.Asset_Name,
                "valueColor": "#333333"
            },
            {
                "subTitle": "Geographies",
                "value": query.location_name,
                "valueColor": "#03AAC9"
            },
            {
                "subTitle": "Org's",
                "value":  query.Region,
                "valueColor": "03AAC9"
            },
            {
                "subTitle": "Breach's cost",
                "value": "480",
                "valueColor": "#333333"
            }
        ]
        other_details = {"title": "OTHER DETAILS",
                         "details": details}
        updated_data = []
        for data in updates:
            last_updates = {
                "updateDateTime": data.update_date,
                "description": data.updates
            }
            updated_data.append(last_updates)
        updates = {
            "title": "UPDATES",
            "data": updated_data
                    }
        data_dict = {
            "incidentStatus": request_status,
            "cards": card,
            "incidentDetails": incident_details,
            "resolutionStatus": resolution_status,
            "otherDetails": other_details,
            "updates": updates
        }
        return data_dict

    @staticmethod
    def update(name, **kwargs):
        """
        Function update an asset from kwargs
        """
        for key, value in kwargs.items():
            setattr(name, key, value)
        name.save()

        return name

    @staticmethod
    def oei_sla_comment(sla, comment):
        """
         Function for OEi sla comment at grid view
        """
        comments = AddOeiComment(
            ticket_id=sla,
            comment=comment
        )
        comments.save()
        return "Comment Added Successfully"

    @staticmethod
    def oei_sla_timeline(response: OeiTimeline):
        """
         Function for OEI sla Timeline view.
        """
        for filter_data in response.request_filters:
            request_filter = filter_data
        for filter_data in response.header_filters:
            header_filter = filter_data
        filters = ("Time-line view of "+request_filter+" - "+header_filter)
        start_time = datetime.strptime(response.start_date, '%Y-%m-%d')
        end_time = datetime.strptime(response.end_date, '%Y-%m-%d')
        total_days = int((end_time - start_time).days)
        delta = relativedelta.relativedelta(end_time, start_time)
        start_date = start_time
        time = []
        within_tickets = []
        outside_tickets = []
        dataset = []
        if total_days <= 31:
            title1 = calendar.month_name[start_date.month]+str(start_date.day)
            title2 = calendar.month_name[end_time.month]+str(end_time.day)
            for x in range(0, total_days+1):
                within_query = (
                    FACT_OEI.objects.filter(CreatedTime__gte=start_date,
                                            CreatedTime__lte=start_date + timedelta(days=1),
                                            Ending_time__lte=end_time,
                                            is_overdue="Within SLA").count())
                within_tickets.append(within_query)
                outside_query = (
                    FACT_OEI.objects.filter(CreatedTime__gte=start_date,
                                            CreatedTime__lte=start_date + timedelta(days=1),
                                            Ending_time__lte=end_time,
                                            is_overdue="Outside SLA").count())
                outside_tickets.append(outside_query)

                time.append(calendar.month_name[start_date.month]+str(start_date.day))
                start_date = start_date + timedelta(days=1)
        if 365 >= total_days > 31:
            if delta.days:
                delta.months += 1
            title1 = calendar.month_name[start_date.month]+str(start_date.year)
            title2 = calendar.month_name[end_time.month]+str(end_time.year)
            for x in range(0, delta.months):
                within_query = (
                    FACT_OEI.objects.filter(CreatedTime__gte=start_date,
                                            CreatedTime__lte=start_date + relativedelta.relativedelta(months=1),
                                            Ending_time__lte=end_time,
                                            is_overdue="Within SLA").count())
                within_tickets.append(within_query)
                outside_query = (
                    FACT_OEI.objects.filter(CreatedTime__gte=start_date,
                                            CreatedTime__lte=start_date + relativedelta.relativedelta(months=1),
                                            Ending_time__lte=end_time,
                                            is_overdue="Outside SLA").count())
                outside_tickets.append(outside_query)
                time.append(calendar.month_name[start_date.month])
                start_date = start_date + relativedelta.relativedelta(months=1)
        if total_days > 365:
            if delta.months:
                delta.years += 1
            if delta.days:
                delta.years += 1
            title1 = start_date.year
            title2 = end_time.year
            for x in range(1, delta.years):
                within_query = (
                    FACT_OEI.objects.filter(CreatedTime__gte=start_date,
                                            CreatedTime__lte=start_date + relativedelta.relativedelta(years=1),
                                            Ending_time__lte=end_time,
                                            is_overdue="Within SLA").count())
                within_tickets.append(within_query)
                outside_query = (
                    FACT_OEI.objects.filter(CreatedTime__gte=start_date,
                                            CreatedTime__lte=start_date + relativedelta.relativedelta(years=1),
                                            Ending_time__lte=end_time,
                                            is_overdue="Outside SLA").count())
                outside_tickets.append(outside_query)
                time.append(start_date.year)
                start_date = start_date + relativedelta.relativedelta(years=1)
        title = str(title1)+"-"+str(title2)
        newdata = {
            "label": "Within SLA",
            "data": within_tickets,
            "backgroundColor": "#16293A"
        }
        newdata1 = {
            "label": "Outside SLA",
            "data": outside_tickets,
            "backgroundColor": "#437DB1"

        }
        dataset.append(newdata)
        dataset.append(newdata1)
        data = {
            "labels": time,
            "datasets": dataset
        }
        returndata = {
            "barChartHeading": {
                "title": filters,
                "subTitle": title
            },
            "chartOptions": {
                "stacked": "false",
                "stepSize": 250,
                "showLendend": "false",
                "legendPosition": "bottom",
                "categoryPercentage": 0.4,
                "scaleLabelofYaxis": {
                    "display": "true",
                    "labelString": "Tickets",
                    "fontStyle": "bold",
                    "fontSize": 14
                },
                "scaleLabelofXaxis": {
                    "display": "true",
                    "labelString": "Time-Period",
                    "fontStyle": "bold",
                    "fontSize": 14
                }
            },
            "data": data
        }
        return returndata

    @staticmethod
    def oei_ticket_timeline(response: OeiTimeline):
        """
         Functions for Oei ticket Timeline views.
        """
        for filter_data in response.request_filters:
            request_filter = filter_data
        for filter_data in response.header_filters:
            header_filter = filter_data
        filters = ("Time-line view of "+request_filter+" - "+header_filter)
        start_time = datetime.strptime(response.start_date, '%Y-%m-%d')
        end_time = datetime.strptime(response.end_date, '%Y-%m-%d')
        total_days = int((end_time - start_time).days)
        delta = relativedelta.relativedelta(end_time, start_time)
        start_date = start_time
        tickets = []
        time = []
        dataset = []
        if total_days <= 31:
            title1 = calendar.month_name[start_date.month]+str(start_date.day)
            title2 = calendar.month_name[end_time.month]+str(end_time.day)
            for x in range(0, total_days+1):
                query = (
                    FACT_OEI.objects.filter(CreatedTime__gte=start_date,
                                            CreatedTime__lte=start_date + timedelta(days=1),
                                            Ending_time__lte=end_time).count()
                )
                tickets.append(query)
                time.append(calendar.month_name[start_date.month]+str(start_date.day))
                start_date = start_date + timedelta(days=1)
        if 365 >= total_days > 31:
            if delta.days:
                delta.months += 1
            title1 = calendar.month_name[start_date.month]+str(start_date.year)
            title2 = calendar.month_name[end_time.month]+str(end_time.year)
            for x in range(0, delta.months):
                query = (
                    FACT_OEI.objects.filter(CreatedTime__gte=start_date,
                                            CreatedTime__lte=start_date + relativedelta.relativedelta(months=1),
                                            Ending_time__lte=end_time).count()
                )
                tickets.append(query)
                time.append(calendar.month_name[start_date.month])
                start_date = start_date + relativedelta.relativedelta(months=1)
        if total_days > 365:
            if delta.months:
                delta.years += 1
            if delta.days:
                delta.years += 1
            title1 = start_date.year
            title2 = end_time.year
            for x in range(1, delta.years):
                query = (
                    FACT_OEI.objects.filter(CreatedTime__gte=start_date,
                                            CreatedTime__lte=start_date + relativedelta.relativedelta(years=1),
                                            Ending_time__lte=end_time).count())
                time.append(start_date.year)
                tickets.append(query)
                start_date = start_date + relativedelta.relativedelta(years=1)
        title = str(title1)+"-"+str(title2)
        newdata = {
            "data": tickets,
            "backgroundColor": "#16293A"
        }
        dataset.append(newdata)
        data = {
            "labels": time,
            "datasets": dataset
        }
        returndata = {
            "barChartHeading": {
                "title": filters,
                "subTitle": title
            },
            "chartOptions": {
                "stacked": "false",
                "stepSize": 250,
                "showLendend": "false",
                "legendPosition": "bottom",
                "categoryPercentage": 0.4,
                "scaleLabelofYaxis": {
                    "display": "true",
                    "labelString": "Tickets",
                    "fontStyle": "bold",
                    "fontSize": 14
                },
                "scaleLabelofXaxis": {
                    "display": "true",
                    "labelString": "Time-Period",
                    "fontStyle": "bold",
                    "fontSize": 14
                }
            },
            "data": data
        }
        return returndata
