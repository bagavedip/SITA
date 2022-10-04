from django.db import models
from django.utils.translation import gettext_lazy as _


class UseCase(models.Model):
    """
    Model to hold data for UseCase data
    """
    usecase = models.CharField(_("use_case"), max_length=200, help_text=_("Use Case"))
    description = models.CharField(_("description"), null=True, max_length=200, help_text=_("Description"))
    default_syntax = models.CharField(_("default_syntax"), null=True, max_length=200, help_text=_("default syntax"))
    category_rule = models.CharField(_("category_rule"), null=True, max_length=200, help_text=_("category_rule"))
    subcategory_rule = models.CharField(_("subcategory_rule"), null=True, max_length=256,
                                        help_text=_("subcategory rule"))
    correlation_rule = models.CharField(_("correlation_rule"), null=True, max_length=256,
                                        help_text=_("correlation rule"))
