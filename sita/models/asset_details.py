from django.db import models
from django.utils.translation import gettext_lazy as _

from sita.models.category import Category
from .process import Process

class AssetsDetails(models.Model):
    """
        Model to hold data of Asset
    """
    id = models.BigAutoField(_("id"), primary_key=True)
    Asset_Name = models.CharField(_("AssetName"), max_length=50, null=True, 
                                    help_text=_("Asset Name"))
    IP_Address = models.CharField(_("IP_Address"), null=True, max_length=50,
                                    help_text=_("IP_Address"))
    Asset_Type = models.CharField(_("Asset_Type"), null=True,max_length=50,
                                    help_text=_("Asset_Type"))
    Category = models.CharField(_("Category"), null=True, max_length=50,
                                    help_text=_("Category"))
    Vendor = models.CharField(_("Vendor"), null=True,max_length=50,
                                    help_text=_("Vendor"))
    Entity = models.CharField(_("Entity"), null=True,max_length=50,
                                    help_text=_("Entity"))
    Geolocation = models.CharField(_("Geolocation"), null=True, max_length=50,
                                    help_text=_("Geolocation"))
    Function = models.CharField(_("Function"), null=True, max_length=50,
                                    help_text=_("Function"))
    Process = models.CharField(_("Process"), null=True, max_length=50,
                                    help_text=_("Process"))
    start_date = models.DateField(_("start_date"), null=True, max_length=50,
                                    help_text=_("start_date"))
    end_date = models.DateField(_("end_date"), null=True, max_length=50,
                                    help_text=_("Delete Date"))
    asset_color = models.CharField(_("asset_color"), null=True, max_length=50,
                                    help_text=_("asset_color"))
    entity_color = models.CharField(_("entity_color"), null=True, max_length=50,
                                    help_text=_("entity_color"))
   












