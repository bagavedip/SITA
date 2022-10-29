from datetime import datetime
import os
import requests
import time
from django.utils.timezone import make_aware


from urllib.parse import urljoin

from sita.models import STG_SIEM, EXTRACTOR_SIEM
from sita.models.audit_siem_stg import Audit_SIEM_STG
from sita.models.audit_siem_extractor import Audit_SIEM


# Remove warnings messages
requests.packages.urllib3.disable_warnings()


class SiemService:
   
    @staticmethod
    def qradar():
        """
         Function to create and update stage_soar table data
        """
        now = datetime.now()
        end_time = datetime.now()
        status = "Failed"
        try:
            audit = Audit_SIEM.objects.filter(status="Success").last()
            print('audit is', audit)
            start_date = audit.start_date
            print('start_date is', start_date)
            last_date = audit.end_date
            queryset = EXTRACTOR_SIEM.objects.filter(created_at__gte=start_date, created_at__lte=last_date).values()
            #queryset = EXTRACTOR_SIEM.objects.all().values()
            print('queryset is', queryset)
            for query in queryset:
                if query.get('log_sources'):
                    final_siem = []
                    for asset in list(eval(query.get('log_sources'))):
                        print('asset is', asset)
                        siem = {
                            "last_persisted_time": datetime.fromtimestamp(int(query.get("last_persisted_time"))/1000) if query.get("last_persisted_time") is not None else None,
                            "username_count": query.get("username_count", None),
                            "description": query.get('description', None),
                            "rules": query.get('rules',None),
                            "event_count": query.get('event_count', None),
                            "flow_count": query.get('flow_count', None),
                            "assigned_to": query.get('assigned_to', None),
                            "security_category_count": query.get('security_category_count', None),
                            "follow_up": query.get('follow_up', None),
                            "source_address_ids": query.get('local_destination_address_ids', None),
                            "source_count": query.get('source_count', None),
                            "inactive": query.get('inactive', None),
                            "protected": query.get('protected', None),
                            "closing_user": query.get('closing_user', None),
                            "destination_networks": query.get('destination_networks', None),
                            "source_network": query.get('source_network', None),
                            "category_count": query.get('category_count', None),
                            "close_time": datetime.fromtimestamp(int(query.get("close_time"))/1000) if query.get("close_time") is not None else None,
                            "remote_destination_count": query.get('remote_destination_count', None),
                            "start_datetime": datetime.fromtimestamp(int(query.get("start_time"))/1000) if query.get("start_time") is not None else None,
                            "magnitude": query.get('magnitude', None),
                            "last_updated_datetime": datetime.fromtimestamp(int(query.get("last_updated_datetime"))/1000) if query.get("last_updated_datetime") is not None else None,
                            "credibility": query.get('credibility', None),
                            "categories": query.get('', None),
                            "severity": query.get('severity', None),
                            "policy_category_count": query.get('policy_category_count', None),
                            "log_sources": asset,
                            "closing_reason_id": query.get('closing_reason_id', None),
                            "device_count": query.get('device_count', None),
                            "first_persisted_time": datetime.fromtimestamp(int(query.get("first_persisted_time"))/1000) if query.get("first_persisted_time") is not None else None,
                            "offense_type": query.get('offense_type', None),
                            "relevance": query.get('relevance', None),
                            "domain_id": query.get('domain_id', None),
                            "offense_source": query.get('offense_source', None),
                            "local_destination_address_ids": query.get('local_destination_address_ids', None),
                            "local_destination_count": query.get('local_destination_count', None),
                            "status": query.get('status', None),
                            "rule_details": query.get('rule_details', None),
                            "seim_id": query.get('siem_id', None),
                            "asset": asset.get('name'),
                            "asset_type": asset.get('type_name'),
                            "asset_id":asset.get("id"),
                            "asset_type_id":asset.get("type_id")
                        }
                        final_siem.append(siem)
                        a = STG_SIEM.objects.update_or_create(defaults=siem, seim_id=query.get('siem_id'), log_sources=asset)
                        #values = STG_SIEM.objects.update_or_create(defaults=siem, seim_id=query.get('siem_id'))
                # this line will create soar data according to given soar dict
                end_time = datetime.now()
                status = "Success"
            return status
        except Exception as e:
            end_time = datetime.now()
            status = "Failed"
            return e
        finally:
            # we are creating Audit record in this block
            audit_dict = {
                "start_date": now,
                "end_date": end_time,
                "status": status
            }
            audit = Audit_SIEM_STG.objects.create(**audit_dict)
            return audit_dict




