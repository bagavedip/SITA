from datetime import datetime
import os
import requests
import time
from django.utils.timezone import make_aware
from django.db.models import OuterRef, Subquery
import json

from urllib.parse import urljoin

from sita.models import STG_SIEM, STG_ITSM, STG_SOAR, AssetsDetails, FACT_INSIGHTS
from shared_stage.models import UseCase

# Remove warnings messages
requests.packages.urllib3.disable_warnings()

class FACTService:
   
    @staticmethod
    def fact():

        # For Accessing the SIEM Details through asset_name
        asset = AssetsDetails.objects.all().values()
        assets = []
        for asset_S in asset:
            asset_name = asset_S.get('Asset_Name')
            assets.append(asset_name)
        SIEM = STG_SIEM.objects.filter(asset__in=assets).values()

        for query in SIEM:
            fact = {
                "asset_id" : query.get('asset_id', None),
                "asset_name"  : query.get('asset', None),
                "asset_type":query.get("asset_type", None),
                "rule_id" : list(eval(query.get('rules')))[0].get('rule_name'),
                "rule_name" : list(eval(query.get('rules')))[0].get('rule_name'),
                "seim_id" : query.get('seim_id', None),
                "events" : query.get('event_count', None),
                "starttime" : query.get('start_datetime', None),
                "description" : query.get('description', None),
            }
            a = FACT_INSIGHTS.objects.update_or_create(defaults=fact, seim_id=query.get('siem_id'), asset_name=query.get('asset'))                        
            
            # For Accessing the Asset Details for all SIEM(Qradar) records
            fact = FACT_INSIGHTS.objects.all().values()
            asset_list_from_fact = []
            for asset_S in fact:
                asset_name = asset_S.get('asset_name')
                asset_list_from_fact.append(asset_name)
                asset_list_from_fact = list(set(asset_list_from_fact))
                Assets = AssetsDetails.objects.filter(Asset_Name__in=asset_list_from_fact).values()
                for id in Assets:
                    asset = id.get('Asset_Name')   
                    """             
                    asset_data =  {
                        "entity_id": id.get('Entity'),
                        "entity_name": id.get('Entity'),
                        "location_id": id.get('Geolocation'),
                        "location_name": id.get('Geolocation'),
                        "function_id": id.get('Function'),
                        "function_name": id.get('Function'),
                        "asset_type": id.get('Asset_Type'),
                    }
                    a = FACT_INSIGHTS.objects.update_or_create(defaults=asset_data, asset_name=asset)
                    print('a is', a)
                    """
                    FACT_INSIGHTS.objects.filter(asset_name=asset).update(entity_id=id.get('Entity'))
                    FACT_INSIGHTS.objects.filter(asset_name=asset).update(entity_name=id.get('Entity'))
                    FACT_INSIGHTS.objects.filter(asset_name=asset).update(location_id=id.get('Geolocation'))
                    FACT_INSIGHTS.objects.filter(asset_name=asset).update(location_name=id.get('Geolocation'))
                    FACT_INSIGHTS.objects.filter(asset_name=asset).update(function_id=id.get('Function'))
                    FACT_INSIGHTS.objects.filter(asset_name=asset).update(function_name=id.get('Function'))
                    FACT_INSIGHTS.objects.filter(asset_name=asset).update(asset_type=id.get('Asset_Type'))
                    FACT_INSIGHTS.objects.filter(asset_name=asset).update(asset_color=id.get('asset_color'))
                    FACT_INSIGHTS.objects.filter(asset_name=asset).update(entity_color=id.get('entity_color'))

            fact = FACT_INSIGHTS.objects.all().values()
            rule_list = []
            for rule in fact:
                rule_name = rule.get('rule_name')
                rule_list.append(rule_name)
                rule_list = list(set(rule_list))
                use_case = UseCase.objects.filter(correlation_rule__in=rule_list).values()
                for id in use_case:
                    rules = id.get('correlation_rule') 

                    """  
                    useCase = {
                        "use_case":id.get('usecase'),
                        "usecase_id":id.get('usecase')
                    }                 
                    a = FACT_INSIGHTS.objects.update_or_create(defaults=useCase, rule_name=rules)
                    """
                    FACT_INSIGHTS.objects.filter(rule_name=rules).update(use_case=id.get('usecase'))
                    FACT_INSIGHTS.objects.filter(rule_name=rules).update(usecase_id=id.get('usecase'))
            
            #For Accesing the SOAR details through SIEM records
            fact = FACT_INSIGHTS.objects.all().values()
            
            seim_id = []
            for id  in fact:
                siem = id.get('seim_id')
                seim_id.append(siem)
                seim_id = list(set(seim_id))
                SOAR = STG_SOAR.objects.filter(TicketIDs__in=seim_id).values()
                for id in SOAR:
                    ticket = id.get('TicketIDs')
                    FACT_INSIGHTS.objects.filter(seim_id=ticket).update(soar_id=id.get('SOAR_ID'))
                    FACT_INSIGHTS.objects.filter(seim_id=ticket).update(ticket_id=id.get('TicketIDs'))
                    FACT_INSIGHTS.objects.filter(seim_id=ticket).update(Suspicious=id.get('Suspicious'))
            
            # For accessing the ITSM data through SOAR details
            #fact = FACT_INSIGHTS.objects.all().values()
            soar_id = []
            for id  in fact:
                soar = id.get('soar_id')
                soar_id.append(soar)
            soar_id = list(set(soar_id))
            ITSM = STG_ITSM.objects.filter(soar_id__in=soar_id).values()
            for id in ITSM:
                soar_id = id.get('soar_id')
                FACT_INSIGHTS.objects.filter(soar_id=soar_id).update(itsm_id=id.get('itsm_id'))
                FACT_INSIGHTS.objects.filter(seim_id=soar_id).update(status=id.get('status_name'))
                FACT_INSIGHTS.objects.filter(seim_id=soar_id).update(priority=id.get('priority_name'))
                FACT_INSIGHTS.objects.filter(soar_id=soar_id).update(group=id.get('group_name'))
                FACT_INSIGHTS.objects.filter(seim_id=soar_id).update(service_category=id.get('service_category_name'))
                FACT_INSIGHTS.objects.filter(seim_id=soar_id).update(assigned_time=id.get('Suspicious'))
                FACT_INSIGHTS.objects.filter(soar_id=soar_id).update(resolution=id.get('resolution_content'))
                #FACT_INSIGHTS.objects.filter(seim_id=ticket).update(assets=id.get('assets'))
                FACT_INSIGHTS.objects.filter(seim_id=soar_id).update(site=id.get('site_name'))
                FACT_INSIGHTS.objects.filter(seim_id=soar_id).update(replys=id.get('TicketIDs'))
                FACT_INSIGHTS.objects.filter(seim_id=soar_id).update(created_time=id.get('created_time_display_value'))
                FACT_INSIGHTS.objects.filter(soar_id=soar_id).update(is_overdue=id.get('is_overdue'))
                FACT_INSIGHTS.objects.filter(seim_id=soar_id).update(due_by_time=id.get('due_by_time'))
                FACT_INSIGHTS.objects.filter(seim_id=soar_id).update(first_response_due_by_time=id.get('first_response_due_by_time_display_value'))
                FACT_INSIGHTS.objects.filter(seim_id=soar_id).update(is_first_response_overdue=id.get('is_first_response_overdue'))
                FACT_INSIGHTS.objects.filter(seim_id=soar_id).update(impact=id.get('impact_name'))
                FACT_INSIGHTS.objects.filter(seim_id=soar_id).update(urgency=id.get('urgency_name'))
                FACT_INSIGHTS.objects.filter(soar_id=soar_id).update(subject=id.get('subject').split('- ')[1])
                #FACT_INSIGHTS.objects.filter(seim_id=ticket).update(comments=id.get('TicketIDs'))
            
        return a

    
    
