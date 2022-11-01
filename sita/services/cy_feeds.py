from rest_framework.response import Response
from sita.models.cy_feeds import CyFeeds

class Cy_FeedsService:
    """
    Service for handling cy feeds
    """
    
    @staticmethod
    def get_cy_feeds():
        """Function to get all feeds of cy pharma"""

        # Query for get all data of CY
        query_data = CyFeeds.objects.all().order_by('-timestamp')
        feeds = []

        #using for loop to store the data
        for data in query_data:
            urls=[]
            url = data.informationSource_references_references
            url = url.strip("[").strip("]").replace("'","")
            urls = url.split(",")
            
            new_feed = {
            "title": data.title,
            "description" :data.descriptions,
            "iconclass" :"fa fa-newspaper-o",
            "linkurls" : urls 
            }
            feeds.append(new_feed)
        return Response({
            "FeedHeader":"CY Firma",
            "Feeds": feeds
        })
