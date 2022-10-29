from django.urls import path
from rest_framework import routers

from .views.assign_task import AssignTaskViewset
from .views.cy_feeds import CyFeeds
from .views.dashboard import DashboardViewSet
from .views.extractor import Extractor
from .views.insights import InsightHub
from .views.perspective import PerspectiveViewSet
from .views.process import ProcessViewSet
from .views.oei import ITSMViewSet
from .views.assets import AssetViewSet
from .views.functions import FunctionViewSet
from .views.entity import EntityViewSet
from .views.geolocation import GeoLocationViewSet
from .views.category import CategoryViewSet
from .views.security_pulse import SecurityPulseViewSet

simple_router = routers.SimpleRouter()

# asset urls
asset = AssetViewSet.as_view({"get": "asset"})
single_asset = AssetViewSet.as_view({"get": "single_asset"})
add_asset = AssetViewSet.as_view({"post": "addasset"})
validate_asset = AssetViewSet.as_view({"post": "validate_asset_csv"})
upload_asset = AssetViewSet.as_view({"post": "upload_asset"})
delete_asset = AssetViewSet.as_view({"delete": "asset_delete"})
update_asset = AssetViewSet.as_view({"put": "update_asset"})

# Function urls
add_function = FunctionViewSet.as_view({"post": "addfunction"})
validate_function = FunctionViewSet.as_view({"post": "validate_function_csv"})
upload_function = FunctionViewSet.as_view({"post": "upload_function"})
delete_function = FunctionViewSet.as_view({"delete": "function_delete"})
update_function = FunctionViewSet.as_view({"put": "update_function"})
functions = FunctionViewSet.as_view({"get": "function"})
single_function = FunctionViewSet.as_view({"get": "single_function_details"})
functiondetails = FunctionViewSet.as_view({"get": "functionlocationentity"})
asset_function = FunctionViewSet.as_view({"get": "function_asset"})

# Geolocation urls
add_location = GeoLocationViewSet.as_view({"post": "addlocation"})
validate_location = GeoLocationViewSet.as_view({"post": "validate_location"})
upload_location = GeoLocationViewSet.as_view({"post": "upload_location"})
delete_location = GeoLocationViewSet.as_view({"delete": "location_delete"})
update_location = GeoLocationViewSet.as_view({"put": "update_location"})
geo_location = GeoLocationViewSet.as_view({"get": "geo_locations"})
single_geo_location = GeoLocationViewSet.as_view({"get": "single_geo_locations"})

# entity
entities = EntityViewSet.as_view({"get": "entities"})
single_entity = EntityViewSet.as_view({"get": "single_entities"})
add_entity = EntityViewSet.as_view({"post": "addentity"})
validate_entity = EntityViewSet.as_view({"post": "validate_entity"})
upload_entity = EntityViewSet.as_view({"post": "upload_entity"})
delete_entity = EntityViewSet.as_view({"delete": "entity_delete"})
update_entity = EntityViewSet.as_view({"put": "update_entity"})

# category
add_category = CategoryViewSet.as_view({"post": "addcategory"})
validate_category = CategoryViewSet.as_view({"post": "validate_category"})
upload_category = CategoryViewSet.as_view({"post": "upload_category"})
category_details = CategoryViewSet.as_view({"get": "category_details"})
single_category = CategoryViewSet.as_view({"get": "single_category_details"})
delete_category = CategoryViewSet.as_view({"delete": "category_delete"})
update_category = CategoryViewSet.as_view({"put": "update_category"})

# process
add_process = ProcessViewSet.as_view({"post": "addprocess"})
validate_process = ProcessViewSet.as_view({"post": "validate_process"})
upload_process = ProcessViewSet.as_view({"post": "upload_process"})
process_details = ProcessViewSet.as_view({"get": "process_details"})
single_process = ProcessViewSet.as_view({"get": "single_process_details"})
delete_process = ProcessViewSet.as_view({"delete": "process_delete"})
update_process = ProcessViewSet.as_view({"put": "update_process"})

# Hub
hub = InsightHub.as_view({"post": "insights_hub"})
insight_tickets = InsightHub.as_view({"post": "insight_tickets"})
grid_master = InsightHub.as_view({"post": "master_data"})
asset_details = InsightHub.as_view({"post": "asset_details"})
oei_chart_data = ITSMViewSet.as_view({"post": "oei_chart_data"})
ticket_dropdown_data = ITSMViewSet.as_view({"post": "ticket_dropdown_data"})
oei_tickets = ITSMViewSet.as_view({"post": "oei_tickets"})
ticket_details = ITSMViewSet.as_view({"post": "ticket_details"})
sla_dropdown_data = ITSMViewSet.as_view({"post": "sla_dropdown_data"})
incident_close = ITSMViewSet.as_view({"post": "incident_close"})
assign_task = InsightHub.as_view({"post": "assign_task"})
hub_timeline = InsightHub.as_view({"post": "hub_timeline"})
oei_ticket_comment = ITSMViewSet.as_view({"post": "oei_ticket_comment"})
incident_comment = InsightHub.as_view({"post": "incident_comment"})
assign_user = AssignTaskViewset.as_view({"post": "assign_user"})
sla_timeline = ITSMViewSet.as_view({"post": "sla_timeline"})
ticket_timeline = ITSMViewSet.as_view({"post": "ticket_timeline"})
add_update = InsightHub.as_view({"post": "add_update"})
daily_metrics = InsightHub.as_view({"post": "daily_metrics"})

perspective_master_dropdown = PerspectiveViewSet.as_view({"post": "perspective_master_dropdown"})
perspective_grid_data = PerspectiveViewSet.as_view({"post": "perspective_grid_data"})
security_pulse_grid_data = SecurityPulseViewSet.as_view({"post": "security_pulse_grid_data"})
add_perspective_record = PerspectiveViewSet.as_view({"post": "add_perspective_record"})
edit_perspective_record_fetch = PerspectiveViewSet.as_view({"post": "edit_perspective_record_fetch"})
edit_perspective_record_submit = PerspectiveViewSet.as_view({"post": "edit_perspective_record_submit"})
perspective_details_data = PerspectiveViewSet.as_view({"post": "perspective_details_data"})
security_pulse_details_data = SecurityPulseViewSet.as_view({"post": "security_pulse_details_data"})
perspective_record_delete = PerspectiveViewSet.as_view({"post": "perspective_record_delete"})
security_pulse_record_delete = SecurityPulseViewSet.as_view({"post": "security_pulse_record_delete"})
edit_security_pulse_record_submit = SecurityPulseViewSet.as_view({"post": "edit_security_pulse_record_submit"})
edit_security_pulse_record_fetch = SecurityPulseViewSet.as_view({"post": "edit_security_pulse_record_fetch"})
add_security_pulse_record = SecurityPulseViewSet.as_view({"post": "add_security_pulse_record"})
fetch_incident_tags = PerspectiveViewSet.as_view({"post": "fetch_incident_tags"})
fetch_asset_tags = PerspectiveViewSet.as_view({"post": "fetch_asset_tags"})
fetch_enity_tags = PerspectiveViewSet.as_view({"post": "fetch_enity_tags"})
dashboard_grid_data = DashboardViewSet.as_view({"post": "dashboard_grid_data"})

feed_data = CyFeeds.as_view({"post": "all_feeds"})

urlpatterns = simple_router.urls
urlpatterns = urlpatterns + [
    path(r"api/v1/update_asset/<int:asset>", update_asset, name="update_asset"),
    path(r"api/v1/delete_asset/<int:asset_id>", delete_asset, name="Asset_Delete"),
    path(r"api/v1/add_asset/", add_asset, name="Add Asset Details"),
    path(r"api/v1/asset/", asset, name="Asset_Details"),
    path(r"api/v1/asset/<int:asset_id>", single_asset, name="Single_Asset_Details"),
    path(r"api/v1/validate_asset/", validate_asset, name="validate Asset Details"),
    path(r"api/v1/upload_asset/", upload_asset, name="Upload Asset File"),

    path(r"api/v1/add_category/", add_category, name="Add Category Details"),
    path(r"api/v1/validate_category/", validate_category, name="validate Category Details"),
    path(r"api/v1/upload_category/", upload_category, name="Upload Category Details"),
    path(r"api/v1/delete_category/<int:category_id>", delete_category, name="Delete Category"),
    path(r"api/v1/update_category/<int:category_id>", update_category, name="Update Category"),
    path(r"api/v1/categories/", category_details, name="Category Details"),
    path(r"api/v1/categories/<int:category_id>", single_category, name="Single Category Details"),

    path(r"api/v1/add_process/", add_process, name="Add Process Details"),
    path(r"api/v1/validate_process/", validate_process, name="validate Process Details"),
    path(r"api/v1/upload_process/", upload_process, name="Upload Process Details"),
    path(r"api/v1/process_details/", process_details, name="Process Details"),
    path(r"api/v1/process_details/<int:process_id>", single_process, name="Single Process Details"),
    path(r"api/v1/delete_process/<int:process_id>", delete_process, name="Delete Process Details"),
    path(r"api/v1/update_process/<int:process_id>", update_process, name="Update Process"),

    path(r"api/v1/add_function/", add_function, name="Add Function"),
    path(r"api/v1/validate_function/", validate_function, name="validate Function Details"),
    path(r"api/v1/upload_function/", upload_function, name="Upload Function Details"),
    path(r"api/v1/function/", functions, name="All Function"),
    path(r"api/v1/function/<int:function_id>", single_function, name="Single Function"),
    path(r"api/v1/delete_function/<int:function_id>", delete_function, name="Delete Function"),
    path(r"api/v1/update_function/<int:function_id>", update_function, name="Update Function"),
    path(r"api/v1/function_details/", functiondetails, name="All Function Details"),

    path(r"api/v1/function/assets/", asset_function, name="Asset for Functions"),

    path(r"api/v1/add_location/", add_location, name="Add Geo Location"),
    path(r"api/v1/validate_location/", validate_location, name="validate location Details"),
    path(r"api/v1/upload_location/", upload_location, name="Upload location Details"),
    path(r"api/v1/geo_locations/", geo_location, name="Geo Location"),
    path(r"api/v1/geo_locations/<int:location_id>", single_geo_location, name="Single Geo Location"),
    path(r"api/v1/delete_location/<int:location_id>", delete_location, name="Delete Geo Location"),
    path(r"api/v1/update_location/<int:location_id>", update_location, name="Update Location"),

    path(r"api/v1/add_entity/", add_entity, name="Add Entity Details"),
    path(r"api/v1/validate_entity/", validate_entity, name="validate Entity Details"),
    path(r"api/v1/upload_entity/", upload_entity, name="Upload Entity Details"),
    path(r"api/v1/entities/", entities, name="Entities_Data"),
    path(r"api/v1/entities/<int:entity_id>", single_entity, name="Single Entities_Data"),
    path(r"api/v1/delete_entity/<int:entity_id>", delete_entity, name="Delete Entities Data"),
    path(r"api/v1/update_entity/<int:entity_id>", update_entity, name="Update Entity"),

    path(r"api/v1/insight_tickets/", insight_tickets, name="insight_tickets"),
    path(r"api/v1/insights/", hub, name="insight_hub"),
    path(r"api/v1/chart-data", hub, name="insight_hub"),
    path(r"api/v1/insight-grid", insight_tickets, name="insight_tickets"),
    path(r"api/v1/insight-grid-master-dropdowns", grid_master, name="grid_master"),
    path(r"api/v1/asset_details/", asset_details, name="asset_details"),
    path(r"api/v1/oei_chart_data/", oei_chart_data, name="oei_chart_data"),
    path(r"api/v1/oei_grid_data/", oei_tickets, name="oei_tickets"),
    path(r"api/v1/ticket_dropdown_data", ticket_dropdown_data, name="ticket_dropdown_data"),
    path(r"api/v1/ticket_details/", ticket_details, name="ticket_details"),
    path(r"api/v1/sla_dropdown_data", sla_dropdown_data, name="sla_dropdown_data"),
    path(r"api/v1/incident_close", incident_close, name="close"),
    path(r"api/v1/assign_task/", assign_task, name="assign_task"),
    path(r"api/v1/hub_timeline/", hub_timeline, name="hub_timeline"),
    path(r"api/v1/oei_ticket_comment", oei_ticket_comment, name="oei_ticket_comment"),
    path(r"api/v1/oei_sla_comment", oei_ticket_comment, name="oei_ticket_comment"),
    path(r"api/v1/insight_incident_comment", incident_comment, name="incident_comment"),
    path(r"api/v1/assign_user/", assign_user, name="assign_user"),
    path(r"api/v1/hub_timeline/", hub_timeline, name="hub_timeline"),
    path(r"api/v1/sla_timeline/", sla_timeline, name="sla_timeline"),
    path(r"api/v1/ticket_timeline/", ticket_timeline, name="ticket_timeline"),
    path(r"api/v1/add_update/", add_update, name="add_update"),
    path(r"api/v1/historical_news_feeds/", feed_data, name="feed_data"),
    path(r"api/v1/daily_metrics/", daily_metrics, name="daily_metrics"),

    path(r"api/v1/perspective_grid_data/", perspective_grid_data, name="perspective_grid_data"),
    path(r"api/v1/perspective_master_dropdown/", perspective_master_dropdown, name="perspective_master_dropdown"),
    path(r"api/v1/security_pulse_grid_data/", security_pulse_grid_data, name="security_pulse_grid_data"),
    path(r"api/v1/add_perspective_record/", add_perspective_record, name="add_perspective_record"),
    path(r"api/v1/edit_perspective_record_submit/", edit_perspective_record_submit,
         name="edit_perspective_record_submit"),
    path(r"api/v1/edit_perspective_record_fetch/", edit_perspective_record_fetch, name="edit_perspective_record_fetch"),
    path(r"api/v1/perspective_details_data/", perspective_details_data, name="perspective_details_data"),
    path(r"api/v1/security_pulse_details_data/", security_pulse_details_data, name="security_pulse_details_data"),
    path(r"api/v1/security_pulse_record_delete/", security_pulse_record_delete, name="security_pulse_record_delete"),
    path(r"api/v1/perspective_record_delete/", perspective_record_delete, name="perspective_record_delete"),
    path(r"api/v1/edit_security_pulse_record_submit/", edit_security_pulse_record_submit,
         name="edit_security_pulse_record_submit"),

    path(r"api/v1/edit_security_pulse_record_fetch/", edit_security_pulse_record_fetch,
         name="edit_security_pulse_record_fetch"),
    path(r"api/v1/add_security_pulse_record/", add_security_pulse_record, name="add_security_pulse_record"),
    path(r"api/v1/fetch_asset_tags/", fetch_asset_tags, name="fetch_asset_tags"),
    path(r"api/v1/fetch_enity_tags/", fetch_enity_tags, name="fetch_enity_tags"),
    path(r"api/v1/fetch_incident_tags/", fetch_incident_tags, name="fetch_incident_tags"),
    path(r"api/v1/dashboard_grid_data/", dashboard_grid_data, name="dashboard_grid_data"),

]
