from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User


class Preference(models.Model):
    """
    Model to hold the user's last used preferences
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        db_index=False,
        verbose_name=_("User's Preference"),
        help_text=_("User's Preference"),
        related_name="+",
    )
    session = models.JSONField(_("session"), default=dict, help_text=_("session"), null=True)

    def __str__(self):
        return self.user + "preference"