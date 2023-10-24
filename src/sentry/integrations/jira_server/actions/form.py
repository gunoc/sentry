from __future__ import annotations

from typing import Any

from django import forms
from django.utils.translation import gettext_lazy as _

from sentry.models.integrations.integration import Integration
from sentry.rules.actions import IntegrationNotifyServiceForm


class JiraServerNotifyServiceForm(IntegrationNotifyServiceForm):
    def clean(self) -> dict[str, Any] | None:
        cleaned_data = super().clean() or {}

        integration = cleaned_data.get("integration")
        try:
            Integration.objects.get(id=integration)
        except Integration.DoesNotExist:
            raise forms.ValidationError(
                _("Jira Server integration is a required field."), code="invalid"
            )
        return cleaned_data