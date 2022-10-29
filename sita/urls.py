from django.urls import path
from rest_framework import routers

from .views.assign_task import AssignTaskViewset
from .views.extractor import Extractor
from .views.hub import InsightHub
from .views.process import ProcessViewSet
from .views.itsm import ITSMViewSet
from .views.assets import AssetViewSet
from .views.functions import FunctionViewSet
from .views.entity import EntityViewSet
from .views.geolocation import GeoLocationViewSet
from .views.category import CategoryViewSet
from .views.staging import Staging
from .views.fact import Fact

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

# Extractor api
itsm = Extractor.as_view({"get": "itsm"})
soar = Extractor.as_view({"get": "soar"})
siem = Extractor.as_view({"get": "siem"})

#Staging api
stg_siem = Staging.as_view({"get":"stg_siem"})
stg_itsm = Staging.as_view({"get":"stg_itsm"})
stg_soar = Staging.as_view({"get":"stg_soar"})

#Fact api
fact = Fact.as_view({"get":"fact"})

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

    # extractor api
    path(r"api/v1/itsm/", itsm, name="itsm"),
    path(r"api/v1/soar/", soar, name="soar"),
    path(r"api/v1/siem/", siem, name="siem"),

    # staging api
    path(r"api/v1/stg_siem/", stg_siem, name="stg_siem"),
    path(r"api/v1/stg_itsm/", stg_itsm, name="stg_itsm"),
    path(r"api/v1/stg_soar/", stg_soar, name="stg_soar"),

    #Fact api
    path(r"api/v1/fact/",fact, name="fact")
]
