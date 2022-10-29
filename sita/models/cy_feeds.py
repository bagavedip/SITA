from django.db import models
from django.utils.translation import gettext as _


class CyFeeds(models.Model):
    feed_id = models.CharField(_("feed_id"), max_length=200, help_text=_("feed_id"), null=True)
    feed_ref_id = models.CharField(_("feed_ref_id"), max_length=200, null=True, help_text=_("feed_ref_id"))
    timestamp = models.DateTimeField(_("timestamp"), null=True, auto_now_add=True, help_text=_("timestamp"))
    title = models.CharField(_("title"), max_length=200, help_text=_("title"), null=True)
    descriptions = models.CharField(_("descriptions"), max_length=1000, null=True, help_text=_("descriptions"))
    shortDescriptions = models.CharField(_("shortDescriptions"), max_length=200, help_text=_("shortDescriptions"), null=True)
    vulnerabilities = models.CharField(_("vulnerabilities"), max_length=500, null=True, help_text=_("vulnerabilities"))
    weaknesses = models.CharField(_("weaknesses"), max_length=200, help_text=_("weaknesses"), null=True)
    configurations = models.CharField(_("configurations"), max_length=200, null=True, help_text=_("configurations"))
    potentialCOAs = models.CharField(_("potentialCOAs"), max_length=200, null=True, help_text=_("potentialCOAs"))
    handling = models.CharField(_("handling"), max_length=200, help_text=_("handling"), null=True)
    relatedExploitTargets = models.CharField(_("relatedExploitTargets"), max_length=200, null=True, help_text=_("relatedExploitTargets"))
    relatedPackages = models.CharField(_("relatedPackages"), max_length=200, help_text=_("relatedPackages"), null=True)
    version = models.CharField(_("version"), max_length=200, null=True, help_text=_("version"))
    informationSource_descriptions = models.CharField(_("informationSource_descriptions"), max_length=200, help_text=_("informationSource_descriptions"), null=True)
    informationSource_identity = models.CharField(_("informationSource_identity"), max_length=200, null=True, help_text=_("informationSource_identity"))
    informationSource_roles = models.CharField(_("informationSource_roles"), max_length=200, null=True, help_text=_("informationSource_roles"))
    informationSource_contributingSources = models.CharField(_("informationSource_contributingSources"), max_length=200, help_text=_("informationSource_contributingSources"), null=True)
    informationSource_time = models.DateTimeField(_("informationSource_time"), null=True, help_text=_("informationSource_time"))
    informationSource_tools = models.CharField(_("informationSource_tools"), null=True, max_length=200, help_text=_("informationSource_tools"))
    informationSource_references_references = models.CharField(_("informationSource_references_references"), max_length=200, help_text=_("informationSource_references_references"), null=True)
    
