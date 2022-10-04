from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """
    Models to hold category data
    """
    id = models.BigAutoField(_("id"), primary_key=True)
    category = models.CharField(_("category"), max_length=50, null=True, help_text=_("Category Name"))
    end_date = models.DateField(_("end_date"), null=True, help_text=_("Delete Date"))
    
    def __str__(self):
        return self.category
