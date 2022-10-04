from django.db import models
from django.utils.translation import gettext_lazy as _

from django_tenants.models import DomainMixin, TenantMixin


class Customer(TenantMixin):
    """
     Model to hold data of customer.
    """
    name = models.CharField(_("name"), max_length=255)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    def __str__(self):
        return self.domain
