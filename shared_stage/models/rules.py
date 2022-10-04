from django.db import models
from .usecase import UseCase
from django.utils.translation import gettext_lazy as _


class Rule(models.Model):
    """
    Model to hold data for Rule data
    """
    rule_name = models.CharField(_("rule_name"), max_length=200, help_text=_("Rule Name"))
    description = models.CharField(_("description"), max_length=200, help_text="Description")
    default = models.CharField(_("default"), max_length=200, help_text="Default")
    usecase = models.ForeignKey(UseCase, verbose_name=_("usecase"), on_delete=models.CASCADE, related_name="+")
    