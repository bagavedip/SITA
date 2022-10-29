import logging
from operator import itemgetter

from sita.models.security_pulse import SecurityPulse
from sita.models.cy_feeds import CyFeeds

logger = logging.getLogger(__name__)


class DashboardService:
    @staticmethod
    def dashboard_grid_data():
        cyfeed = CyFeeds.objects.all().order_by('-timestamp')
        feeds = []
        # using for loop to store the data
        for data in cyfeed:
            url = data.informationSource_references_references
            url = url.strip("[").strip("]").replace("'","")
            urls = url.split(",")

            new_feed = {
                "title": data.title,
                "description": data.descriptions,
                "IsExternal": True,
                "links": urls[0],
                "published_date": data.timestamp
            }
            feeds.append(new_feed)
        security_pulse = SecurityPulse.objects.all().order_by('-updated_at')
        security_pulse_list = []
        for data in security_pulse:
            new_feed = {
                "title": data.security_pulse_title,
                "id": str(data.id),
                "IsExternal": False,
                "published_date": data.updated_at,
                "description": data.main_title
            }
            security_pulse_list.append(new_feed)
        query_data = security_pulse_list + feeds
        query_data = sorted(query_data, key=itemgetter('published_date'), reverse=True)
        return query_data
