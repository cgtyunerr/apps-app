"""Campaign schemas."""
from datetime import datetime
from typing import TypeAlias

from pydantic import BaseModel


class ServiceCampaignSchema(BaseModel):
    """Service campaign schema.

    Parameters:
        service_campaign_id: The service campaign id.
        title: The title of the campaign.
        created_at: The creation date of the campaign.
        active: Whether the campaign is active.
    """
    service_campaign_id: int
    title: str
    created_at: datetime
    active: bool

ServiceCampaignsSchema: TypeAlias = list[ServiceCampaignSchema]
