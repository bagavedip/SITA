import logging

from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from sita.constants.dataset import Dataset
from sita.models import STG_ITSM
from sita.models.add_oei_comment import AddOeiComment
from sita.serializers.oei_timeline import OeiTimeline
from sita.serializers.itsm import ITSMSerializer
from sita.serializers.oei_serializers import OeiSerializer
from sita.serializers.oei_ticket_details import TicketDetailsSerializer
from sita.services.itsm import ITSMService
import json
from collections import defaultdict as dd


logger = logging.getLogger(__name__)


class ITSMViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    queryset = ITSMService.get_queryset()

    def convert_data(self, dataset):
        if len(dataset) == 0:
            pass
        else:
            keys = dataset[0].keys()
            key_var = ""
            nested_dict_str = "dd(list)"

            key_index = 0
            for key in keys:
                if key_index < len(keys) - 1:
                    if key_index < len(keys) - 2:
                        nested_dict_str = "dd(lambda: " + nested_dict_str + ")"
                    key_var = key_var + "[data.get('" + key + "')]"
                    key_index += 1

            nested_dict = eval(nested_dict_str)
            # sala = STG_ITSM.objects.filter(sla_name=keys.).count()
            temp1 = "nested_dict" + key_var + ".append(data.get('events'))"
            # Note that variable name here has to be "data" as this is what is used to build the executable string above
            for data in dataset:
                exec(temp1)
            nested_dict = json.loads(json.dumps(nested_dict))
            return nested_dict

    def build(self, dictionary, depth, datasets):
        keys = dictionary.keys()
        # ("tyring to add", str(keys), " at depth ", depth)
        datasets[depth]['labels'].extend(list(keys))
        depth += 1
        for key in keys:
            value = dictionary.get(key)
            if type(value) is dict:
                self.build(value, depth, datasets)

    def build_response(self, req_data, data):

        labels = req_data.get('filterOptions').get('headerFilters')
        labels.append(req_data.get('filterOptions').get('headerOption'))

        id = 1
        datasets = []
        for label in labels:
            ds = Dataset().init_response_dataset()
            ds['id'] = id
            ds['label'] = label
            id += 1
            datasets.append(ds)

        depth = 0
        self.build(data, depth, datasets)
        return datasets

    def calculate_events(self, data):
        last_event_count = 0
        for key, value in data.items():
            if type(value) is dict:
                last_event_count = self.calculate_events(value)
            else:
                last_event_count = last_event_count + value[0]
        return last_event_count

    def update_events(self, data):
        if data is not None:
            for key, value in data.items():
                events = self.calculate_events(value)
                data[key]['events'] = events

    def request_modes(self, request):
        try:
            Total_modes = []
            for mode in self.queryset.values():
                    Total_modes.append(mode.get('Request_mode'))
            # Created blank dict, added asset_type wise count in blank dict
            mode_types = dict()  
            for modes in Total_modes:
                mode_types[modes] = mode_types.get(modes, 0) + 1
            # added total asset types in dict by using other asset type counts
            mode_types['Total Requests'] = sum(mode_types.values())
            data = mode_types
            return Response(
                {
                    "Status": "Success",
                    "Data": data
                }
            )
        except:
            return Response(
                {
                    "Status": "Failed",
                    "Message": "You Don't have data"
                }
            )

    def ticket_dropdown_data(self, request):
        """
         Ticket dropdown data for grid view.
        """

        logger.debug(f"Received request body {request.data}")
        categories = STG_ITSM.objects.values_list('is_overdue').distinct()
        category_dropdown = [{
                        "value": "Select",
                        "label": "Category"
                    }]
        priorities = STG_ITSM.objects.values_list('Priority').distinct()
        priority_dropdown = [{
                        "value": "Select",
                        "label": "Priority"
                    }]
        statuses = STG_ITSM.objects.values_list('RequestStatus').distinct()
        status_dropdown = [{
                        "value": "Select",
                        "label": "Status"
                    }]
        reopened = STG_ITSM.objects.values_list('reopened').distinct()
        reopened_dropdown = [{
                        "value": "Select",
                        "label": "Reopened"
                    }]
        for category in categories:
            new_category = {"value":category,
                        "label":category}
            category_dropdown.append(new_category)
        for priority in priorities:
            new_priority = {"value":priority,
                        "label":priority}
            priority_dropdown.append(new_priority)
        for s in statuses:
            new_status = {"value":s,
                        "label":s}
            status_dropdown.append(new_status)
        for reopen in reopened:
            new_reopened = {"value":reopen,
                        "label":reopen}
            reopened_dropdown.append(new_reopened)
        
        response = [
                {
                    "id": "Category ",
                    "dropdownoption": category_dropdown
                },
                {
                    "id": "Priority",
                    "dropdownoption": priority_dropdown
                },
                {
                    "id": "Status",
                    "dropdownoption": status_dropdown
                }, {
                "id": "Service",
                "dropdownoption": [
                    {
                        "value": "Select",
                        "label": "Service | Select"
                    },
                    {
                        "label": "SOC",
                        "value": "SOC"
                    }
                ]
            }, {
                "id": "Reopened %",
                "dropdownoption": reopened_dropdown
            }, {
                "id": "First response Time",
                "dropdownoption": [
                    {
                        "value": "Select",
                        "label": "First response Time | Select"
                    },
                    {
                        "label": "All",
                        "value": "All"
                    }
                ]
            }
        ]

        return Response(response, status=status.HTTP_201_CREATED)

    def sla_dropdown_data(self, request):
        """
         SLA dropdown data for grid view.
        """
        logger.info(f"request is {request.data}")
        data = [{
                "id": "Service",
                "dropdownoption": [
                    {
                        "value": "Select",
                        "label": "Service"
                    },
                    {
                        "label": "SOC",
                        "value": "SOC"
                    }
                ]
                }
                ]
        return Response(data, status=status.HTTP_201_CREATED)

    def oei_tickets(self, request):
        """
         OEI ticket details view.
        """
        logger.debug(f"Received request body {request.data}")
        response_obj = TicketDetailsSerializer(request)
        data = ITSMService.get_tickets(response_obj)
        return Response(response_obj.get_response(data), status=status.HTTP_201_CREATED)

    def ticket_details(self, request):
        """
          Functions for details page of OEI tickets
        """
        request_data = request.data
        ticket = request_data.get("requestId", None)
        queryset = ITSMService.asset_details(ticket)
        return Response(queryset, status=status.HTTP_201_CREATED)

    def oei_chart_data(self, request, **kwargs):
        """
         Function to get OEi donut chart Data.
        """
        logger.info("Validating data for Log In.")
        serializser = OeiSerializer(request)
        result = ITSMService.get_oei(serializser)
        hirarchial_data = self.convert_data(result)
        if len(serializser.datasets) !=1:
            self.update_events(hirarchial_data)
        query_data = STG_ITSM.objects.filter(CreatedTime__gte=serializser.start_date,
                                         Ending_time__lte=serializser.end_date).count()
        data = STG_ITSM.objects.filter(CreatedTime__gte=serializser.start_date,
                                   Ending_time__lte=serializser.end_date, is_overdue='1').count()
        total_ticket = query_data
        legends = []
        if total_ticket == 0:
            return Response(None, status=status.HTTP_201_CREATED)
        else:
            percentage = round((data * 100) / query_data)
            Compliance = percentage
            final_response = {
                "charFooter": {
                    "label": "SLA  Compliance",
                    "value": str((Compliance)) + "%",
                    "valueFontColor": "green"
                },
                "legends": {
                    "header": request.data.get('filterOptions').get('headerOption'),
                    "items": legends
                },
                "doughnutlabel": {
                    "labels": [
                        {
                            "text": "Tickets {total_ticket}".format(total_ticket=total_ticket),
                            "font": {
                                "size": "25"
                            },
                            "color": "black"
                        },
                    ]
                },
                "datasets": serializser.datasets
            }
            return Response(final_response, status=status.HTTP_201_CREATED)

    def incident_close(self, request):
        """
         Function to incident close at ticket details page
        """
        incidentId = request.data.get("incidentId", None)
        data = {
            "status": True
        }
        return Response(data, status=status.HTTP_201_CREATED)

    def oei_ticket_comment(self, request):
        """
        Function which update comment information.
        """
        logger.debug(f"Parsed request body {request.data}")
        # Validating incoming request body
        serializer = request.data
        # update comment in sla and ticket information
        logger.debug("Database transaction started")
        try:
            with transaction.atomic():
                selected_incidents = serializer.get("selectedIncidents")
                comment = serializer.get("Comment")
                comment = ITSMService.oei_sla_comment(selected_incidents, comment)
            logger.debug("Database transaction finished")
            # response formatting
            response_data = {
                "msg": comment,
                "status": True
            }
            return Response(response_data)
        except UnboundLocalError:
            return Response({"error": "there is no such selectedIncidents."})

    def sla_timeline(self, request):
        """
         SLA dropdown data for grid view.
        """
        logger.info(f"request is {request.data}")
        serializser = OeiTimeline(request)
        result = ITSMService.oei_sla_timeline(serializser)
        return Response(result, status=status.HTTP_200_OK)

    def ticket_timeline(self, request):
        """
         Function for time timeline view in OEI(ITSM)
        """
        serializser = OeiTimeline(request)
        result = ITSMService.oei_ticket_timeline(serializser)
        return Response(result, status=status.HTTP_200_OK)
