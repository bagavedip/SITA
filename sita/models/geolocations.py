from django.db import models
from .entity import Entity
from django.utils.translation import gettext_lazy as _


class GeoLocation(models.Model):
    """
    Models to hold Geolocations data
    """
    id = models.BigAutoField(_("id"), primary_key=True)
    location = models.CharField(_("location"), max_length=50, null=True, help_text=_("Location Name"))
    entity_id = models.ForeignKey(Entity, verbose_name=_("entity_id"), on_delete=models.CASCADE, related_name="+",
                                  help_text=_("entity_id"))
    end_date = models.DateField(_("end_date"), null=True, help_text=_("Delete Date"))
    
    def __str__(self):
        return self.location
