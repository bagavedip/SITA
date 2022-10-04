from django.db import models
from django.utils.translation import gettext as _


class Source(models.Model):
    """
    Model to hold data for Source data
    """
    class ModelName(models.TextChoices):
        SIEM = "SIEM", _("SIEM")
        SOAR = "SOAR", _("SOAR")
        ITSM = "ITSM", _("ITSM")

    class FileType(models.TextChoices):
        JSON = "JSON", _("json")
        EXCEL = "EXCEL", _("excel")
        CSV = "CSV", _("csv")
    name = models.CharField(
        _("source name"), max_length=100, choices=ModelName.choices, null=True, help_text="source name")
    type = models.CharField(
        _("file type"), max_length=100, choices=FileType.choices, null=True, help_text="file type")
    credentials = models.JSONField(
        _("credentials"), default=dict, help_text="credentials"
    )

    def __str__(self):
        return self.name
