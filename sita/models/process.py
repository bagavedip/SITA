from django.db import models
from django.utils.translation import gettext_lazy as _
from .functions import Function

class Process(models.Model):
    """
    Model to hold Process data
    """
    id = models.BigAutoField(_("id"), primary_key=True)
    process = models.CharField(_("process"), max_length=50, null=True, help_text="Process Name")
    function_id = models.ForeignKey(Function, verbose_name=_("function_id"), on_delete=models.CASCADE,
                                    help_text=_("Function Name"))
    end_date = models.DateField(_("end_date"), null=True, help_text=_("Delete Date"))
    
    def __str__(self):
        return self.process
