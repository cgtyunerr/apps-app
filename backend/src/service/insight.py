"""Insight service."""
from pydantic import InstanceOf, validate_call
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .service import Service
from src.domain import InsightApiCall
from src.model import Insight, CampaignCreative
from src.schema import InsightsSchema, InsightSchema

insight_api_call: InsightApiCall = InsightApiCall()

class InsightService(Service):
    """Insight service.

    Methods:
        get_all_insights: Get all insights that are related to campaign.
    """
    @validate_call
    async def get_all_insights(
        self,
        session: InstanceOf[AsyncSession],
        campaign_id: int,
    ) -> InsightsSchema:
        """Get all insights that are related to campaign.

        Arguments:
            session: Database session.
            campaign_id: ID of the campaign.

        Returns:
            InsightsSchema.

        Raises:
            NotFoundError.
        """
        query_result = await session.execute(
            select(Insight)
            .join(CampaignCreative, Insight.campaign_creative_id == CampaignCreative.id)
            .filter(CampaignCreative.campaign_id == campaign_id)
        )
        insights = query_result.scalars().all()
        result: InsightsSchema = []
        for insight in insights:
            result.append(
                InsightSchema(
                    id=insight.id,
                    impressions=insight.impressions,
                    cpi=insight.cpi,
                    ctr=insight.ctr,
                    cpm=insight.cpm,
                    ipm=insight.ipm,
                    campaign_creative_id=insight.campaign_creative_id,
                    created_at=insight.created_at,
                )
            )

        return result
