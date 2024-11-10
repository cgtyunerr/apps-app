"""Insight schemas."""
from datetime import datetime
from typing import TypeAlias

from pydantic import BaseModel

class InsightSchema(BaseModel):
    """Insight schema.
    Parameters:
        id: insight id.
        campaign_creative_id: campaign creative id.
        created_at: creation date.
        impressions: impressions.
        cpi: int.
        ctr: int.
        cpm: int.
        imp: int.
    """
    id: int
    campaign_creative_id: int
    created_at: datetime
    impressions: int
    cpi: int
    ctr: int
    cpm: int
    imp: int

InsightsSchema: TypeAlias = list[InsightSchema]
