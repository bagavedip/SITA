import calendar
from datetime import datetime,timedelta
from dateutil import relativedelta

from sita.models.add_comment import AddComment
from sita.models.assign_task import AssignTask
from sita.models.fact_insights import FACT_INSIGHTS
from sita.models.insights_update import HubUpdate
from django.db.models import Sum,Count

from sita.serializers.hub import InsightsSerializer
from sita.serializers.hub_timeline import HubTimeline


class HubService:
    """
     Services for Hub models
    """

    @staticmethod
    def get_queryset():
        queryset = FACT_INSIGHTS.objects.all()
        return queryset

    @staticmethod
    def get_insights(response_obj: InsightsSerializer):
        query_data = (
            FACT_INSIGHTS.objects.filter(starttime__gte=response_obj.start_date,endtime__lte=response_obj.end_date).
            values(*response_obj.model_group_map).order_by().annotate(events=Count('itsm_id')))
        response_obj.set_requst_queryset(query_data)
        incidents = (
            FACT_INSIGHTS.objects.filter(starttime__gte=response_obj.start_date,endtime__lte=response_obj.end_date)
            .values('priority').order_by().annotate(events=Count('itsm_id')))
        for row in incidents:
            response_obj.donut_center[row.get('priority')] = row.get('events')
        return query_data

    @staticmethod
    def get_legends(response_obj: InsightsSerializer):
        query_data = (
            FACT_INSIGHTS.objects.filter(starttime__gte=response_obj.start_date,endtime__lte=response_obj.end_date).
            values(response_obj.legend_filter).distinct(response_obj.legend_filter))
        legends = []
        for row in query_data:
            legends.append(row.get(response_obj.legend_filter))
        return legends

    @staticmethod
    def asset_details(incident):
        data = HubService.get_queryset().filter(soar_id=incident)
        updates = HubUpdate.objects.all().filter(soar_id=incident).order_by('-update_date')[:6]
        desktop = 0
        laptop = 0
        mobile = 0
        entityes = 0
        assets = str(data.count())
        asset_names = []
        for types in data:
            asset_names.append(types.asset_name)
            asset_type = types.asset_type
            entity = types.entity_name
            if entity:
                entityes = entityes + 1
            if asset_type == "Desktop":
                desktop = desktop + 1
            if asset_type == "Laptop":
                laptop = laptop + 1
            if asset_type == "Mobile":
                mobile = mobile + 1
        asset_types = (
                "MOBILE" + "~" + str(mobile) + "*" + "DESKTOP" + "~" + str(desktop) + "*" + "LAPTOP" + "~" + str(laptop)
        )
        entity_count = str(entityes)
        assets = assets + " :" + str(asset_names)
        for query in data:
            incident_status = {"text": query.status,"color": "#ffc107"}
            time_to_close = (query.assigned_time - query.starttime)
            time = int(abs(time_to_close).total_seconds() / 3600)
            time_to_close = {"cardTitle": str(time) + " Hrs","textColor": "#ffc107","cardSubTitle": "Time to close",
                             "cardIcon": "OrangeWait"}
            suspicious = {"cardTitle": query.Suspicious,"textColor": "#ffc107","cardSubTitle": "Expected closure",
                          "cardIcon": "OrangeChartLineUp"}
            if query.priority == "2. Alta":
                priority = "RED"
                color = "#ff0000"
                card_icon = "RedCaution"
            elif query.priority == "4. Baja":
                priority = "Green"
                color = "#00FF00"
                card_icon = "GreenCaution"
            else:
                priority = "Orange"
                color = "#FFA500"
                card_icon = "OrangeCaution"
            tread_level = {"cardTitle": priority,"textColor": color,"cardSubTitle": "Threat Level",
                           "cardIcon": card_icon}
            card = [tread_level,time_to_close,suspicious]
            incident_details = {"title": "INCIDENT DETAILS",
                                "description": "ITSM Case: " + query.itsm_id + "\n SOAR ID:" + query.soar_id,
                                }
            resolution_status = {
                "title": "RESOLUTION STATUS",
                "resolutionDetails": {
                    "title": "Resolution Details",
                    "description": query.resolution,
                    "isEditable": "true"
                },
                "resolutionOwner": {

                    "title": "Resolution Owner",
                    "description": query.group,
                    "isEditable": "true"
                }
            }
            details = [{
                "subTitle": "Assets Affected",
                "value": assets,
                "valueColor": "#333333"
            },
                {
                    "subTitle": "Assets Type",
                    "value": asset_types,
                    "valueColor": "#333333"
                },
                {
                    "subTitle": "Geo",
                    "value": query.location_name,
                    "valueColor": "#03AAC9"
                },
                {
                    "subTitle": "Entities",
                    "value": entity_count,
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
            "incidentStatus": incident_status,
            "cards": card,
            "incidentDetails": incident_details,
            "resolutionStatus": resolution_status,
            "otherDetails": other_details,
            "updates": updates
        }
        return data_dict

    @staticmethod
    def hub_timeline(response: HubTimeline):
        for filter_data in response.request_filters:
            request_filter = filter_data
        for filter_data in response.header_filters:
            header_filter = filter_data
        filters = ("Time-line view of " + request_filter + " - " + header_filter)
        start_time = datetime.strptime(response.start_date,'%Y-%m-%d')
        end_time = datetime.strptime(response.end_date,'%Y-%m-%d')
        total_days = int((end_time - start_time).days)
        delta = relativedelta.relativedelta(end_time,start_time)
        start_date = start_time
        incidents = []
        time = []
        dataset = []
        if total_days <= 31:
            title1 = calendar.month_name[start_date.month] + str(start_date.day)
            title2 = calendar.month_name[end_time.month] + str(end_time.day)
            for x in range(0,total_days + 1):
                query = (
                    FACT_INSIGHTS.objects.filter(starttime__gte=start_date,starttime__lte=start_date + timedelta(days=1),
                                       endtime__lte=end_time).count()
                )
                incidents.append(query)
                time.append(calendar.month_name[start_date.month] + str(start_date.day))
                start_date = start_date + timedelta(days=1)
        if 365 >= total_days > 31:
            if delta.days:
                delta.months += 1
            title1 = calendar.month_name[start_date.month] + str(start_date.year)
            title2 = calendar.month_name[end_time.month] + str(end_time.year)
            for x in range(0,delta.months):
                query = (
                    FACT_INSIGHTS.objects.filter(starttime__gte=start_date,
                                       starttime__lte=start_date + relativedelta.relativedelta(months=1),
                                       endtime__lte=end_time).count())
                incidents.append(query)
                time.append(calendar.month_name[start_date.month])
                start_date = start_date + relativedelta.relativedelta(months=1)
        if total_days > 365:
            if delta.months:
                delta.years += 1
            if delta.days:
                delta.years += 1
            title1 = start_date.year
            title2 = end_time.year
            for x in range(1,delta.years):
                query = (
                    FACT_INSIGHTS.objects.filter(starttime__gte=start_date,
                                       starttime__lte=start_date + relativedelta.relativedelta(years=1),
                                       endtime__lte=end_time).count())
                time.append(start_date.year)
                incidents.append(query)
                start_date = start_date + relativedelta.relativedelta(years=1)
        title = str(title1) + "-" + str(title2)
        newdata = {
            "data": incidents,
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
                    "labelString": "Incidents",
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
    def update(name,**kwargs):
        """
        Function update an asset from kwargs
        """
        for key,value in kwargs.items():
            setattr(name,key,value)
        name.save()

        return name

    @staticmethod
    def incident_comment(selectedIncidents,comment):
        comment = AddComment(
            incident_id=selectedIncidents,
            comment=comment
        )
        comment.save()
        return "Comment Added Successfully !!"

    @staticmethod
    def assign_user(selectedIncidents,user):
        assign_list = []
        for incidents in selectedIncidents:
            queryset = AssignTask.objects.filter(incident_id=incidents)
            if queryset:
                return "already Assigned"
            else:
                assign_list.append(
                    AssignTask(
                        incident_id=incidents,
                        assigned_user=user
                    ))
        AssignTask.objects.bulk_create(assign_list)
        return "Task successfully Assigned !!"

    @staticmethod
    def add_update(soar_id,update,update_by):
        update = HubUpdate(
            soar_id=soar_id,
            updates=update,
            updated_by=update_by
        )
        update.save()
        return "Update Added Successfully !!"

