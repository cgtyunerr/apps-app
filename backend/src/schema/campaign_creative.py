"""Campaign creative schemas."""
from datetime import datetime
from typing import TypeAlias

from pydantic import BaseModel

class ServiceCampaignCreativeSchema(BaseModel):
    """Campaign creative service model.

    Parameters:
        id: campaign creative id.
        status: campaign creative status.
        created_at: campaign creative creation date.
        asset_id: campaign creative asset id.
    """
    id: int
    status: str
    created_at: datetime
    asset_id: int

ServiceCampaignCreativesSchema: TypeAlias = list[ServiceCampaignCreativeSchema]

class DatabaseCampaignCreativeSchema(ServiceCampaignCreativeSchema):
    """Campaign creative database model.

    Parameters:
        campaign_id: campaign id.
    """
    campaign_id: int

DatabaseCampaignCreativesSchema: TypeAlias = list[DatabaseCampaignCreativeSchema]
