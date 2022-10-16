# Signal handlers have to be imported on app ready state to avoid circular imports
# pylint: disable=import-outside-toplevel

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class YewtailAppConfig(AppConfig):
    """Django admin yewtail app config"""

    name = "yewtail"
    label = "yewtail"
    verbose_name = _("Django Admin Yew-Tailwind")
