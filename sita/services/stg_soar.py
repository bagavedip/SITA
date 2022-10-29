from datetime import datetime
from sita.models import EXTRACTOR_SOAR, STG_SOAR, EXTRACTOR_ITSM, EXTRACTOR_SIEM, STG_SIEM, STG_ITSM
from sita.models.audit_siem_stg import Audit_SIEM_STG
from sita.models.audit_soar_stg import Audit_SOAR_STG
from sita.models.audit_itsm_stg import Audit_ITSM_STG
from sita.models.audit_soar_extractor import Audit_SOAR_EXTRACTOR


class SoarService:    
    @staticmethod
    def soar():

        """
         Function to create and update stage_soar table data
        """
        now = datetime.now()
        end_time = datetime.now()
        status = "Failed"
        try:
            print("Hello")
            audit = Audit_SOAR_EXTRACTOR.objects.filter(status="Success").last()
            print('audit is', audit)
            start_date = audit.start_date
            last_date = audit.end_date
            queryset = EXTRACTOR_SOAR.objects.filter(created_at__gte=start_date, created_at__lte=last_date)
            print('queryset is', queryset)
            a = []
            for row in queryset:
                closing_time = int(row.ClosingTime)
                print('closing time is', closing_time)
                print('ticket id is', row.TicketIDs.split('_')[0])
                soar = {
                    "SOAR_ID": int(row.SOAR_ID),
                    "AssignedUser": row.AssignedUser,
                    "Title": row.Title,
                    "Time": row.Time,
                    "Tags": row.Tags,
                    "Products": row.Products,
                    "Incident": row.Incident,
                    "Suspicious": row.Suspicious,
                    "Important": row.Important,
                    "Ports": int(row.Ports),
                    "Outcomes": row.Outcomes,
                    "Status": row.Status,
                    "Environment": row.Environment,
                    "Priority": row.Priority,
                    "Stage": row.Stage,
                    "TicketIDs": row.TicketIDs.split('_')[0],
                    "ClosingTime": datetime.fromtimestamp(closing_time/1000),
                    "Sources": row .Sources,
                    "Reason": row.Reason,
                    "RootCause": row.RootCause,
                    "Case_id": row.Case_id,
                    "AlertsCount": row.AlertsCount
                }

                soar_id = int(row.SOAR_ID)
                print('soar id is', soar_id)

                # this line will create soar data according to given soar dict
                print('soar is', soar)
                a = STG_SOAR.objects.update_or_create(defaults=soar, SOAR_ID=row.SOAR_ID)
                print('a is', a)
                end_time = datetime.now()
                status = "Success"
            return a
        except Exception as e:
            print('exception is',e)
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
            audit = Audit_SOAR_STG.objects.create(**audit_dict)
            return audit_dict