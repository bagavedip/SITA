import json
import requests
from datetime import datetime
from sita.models import EXTRACTOR_SOAR
from sita.models.audit_soar_extractor import Audit_SOAR_EXTRACTOR


class SoarService:
    @staticmethod
    def get_all_cases():
        now = datetime.now()
        end_time = datetime.now()
        status = "Failed"

        # query to find last success record in audit_table
        queryset = Audit_SOAR_EXTRACTOR.objects.all() # filter(status="Success").last()
        if queryset:
            time = queryset.end_date
        else:
            time = datetime.now()
        try:
            start_time = int(time.timestamp() * 1000)
            endtime = int(now.timestamp() * 1000)

            url = "https://192.168.200.98/api/external/v1/cases/GetCaseCardsByRequest"
            payload = {
                "pageSize": 20,
                "pageNumber": 1,
                "liveQueueSettings": {
                        "startTimeUnixTimeInMs": start_time,
                        "endTimeUnixTimeInMs": endtime
                    }
                }
            headers = {
                'AppKey': 'a936681c-db8c-49b5-be95-e56e943f6426',
                'Content-type': 'application/json',
                'Accept': 'application/json'
            }
            response = requests.post(url,  headers=headers, data=str(payload),  verify=False)

            # fetch all records from url and store it in output
            output = json.loads(response.text)
            numbers = []
            for data in output['caseCards']:
                # fetch id for single record url
                keys = data.get('id')
                numbers.append(keys)
                a = []
                for n in numbers:
                    headers = {'AppKey': 'a936681c-db8c-49b5-be95-e56e943f6426'}
                    url = "https://192.168.200.98/api/external/v1/cases/GetCaseFullDetails/" + str(n)
                    payload = {}
                    response = requests.request("GET", url, headers=headers, data=payload, verify=False)

                    # fetch all records from url and store it in output
                    output = json.loads(response.text)
                    priority = output.get('alerts')[0].get('additionalProperties').get('priority')
                    environment = output.get('alerts')[0].get('additionalProperties').get('environment')
                    last_updated_time = output.get('alerts')[0].get('additionalProperties').get('last_updated_time')
                    products = output.get('alerts')[0].get('additionalProperties').get('deviceProduct')
                    for source in output.get('alerts')[0].get('securityEventCards'):
                        sources = source.get('sources')
                        port = source.get('port')
                        outcome = source.get('outcome')
                        times = int(source.get('time'))
                    soar = {
                        "SOAR_ID": output.get('id', None),
                        "AssignedUser": output.get('assignedUserName', None),
                        "Title": output.get('title', None),
                        "Time": datetime.fromtimestamp((times/1000)),
                        "Tags": output.get('tags', None),
                        "Products": products,
                        "Incident": output.get('isIncident', None),
                        "Suspicious": output.get('hasSuspiciousEntity', None),
                        "Important": output.get('isImportant', None),
                        "Ports": port,
                        "Outcomes": outcome,
                        "Status": output.get('status', None),
                        "Environment": environment,
                        "Priority": priority,
                        "Stage": output.get('stage', None),
                        "TicketIDs": output.get("alerts", None)[0].get('ticketId'),
                        'ClosingTime': last_updated_time,
                        "Sources": sources,
                        "Reason": output.get("", None),
                        "RootCause": output.get("", None),
                        "Case_id": output.get('id', None),
                        "AlertsCount": output.get("", None),
                    }
                    a.append(output.get("id"))
                # this line will create soar data according to given soar dict
            values = EXTRACTOR_SOAR.objects.update_or_create(defaults=soar, SOAR_ID=a)
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
            audit = Audit_SOAR_EXTRACTOR.objects.create(**audit_dict)
            return audit_dict
