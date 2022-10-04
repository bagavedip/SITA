from django.db import models
from django.utils.translation import gettext_lazy as _

from sita.models.category import Category
from .process import Process


class Assets(models.Model):
    """
        Model to hold data of Asset
    """

    class Criticalities(models.TextChoices):
        High = "High", _("High")
        Medium = "Medium", _("Medium")
        Critical = "Critical", _("Critical")

    id = models.BigAutoField(_("id"), primary_key=True)
    AssetName = models.CharField(_("AssetName"), max_length=50, null=True, help_text=_("Asset Name"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text="Asset Category")
    criticality = models.CharField(_("criticality"), max_length=100, choices=Criticalities.choices,
                                   default="Low", help_text=_("Criticality"))
    process_id = models.ForeignKey(Process, verbose_name=_("process_id"), on_delete=models.CASCADE,
                                    help_text=_("Process Name"))
    created = models.DateField(_("created"), null=True, auto_now_add=True, help_text=_("created"))
    end_date = models.DateField(_("end_date"), null=True, help_text=_("Delete Date"))

    def __str__(self):
        return self.AssetName
