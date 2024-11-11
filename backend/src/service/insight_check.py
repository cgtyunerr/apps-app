"""Insight check."""
from typing import TypeAlias

from pydantic import BaseModel, ConfigDict, validate_call
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import database_session_manager
from src.domain import CampaignApiCall, InsightApiCall
from src.model import Insight
from src.schema import InsightsSchema, ServiceCampaignsSchema
from .service import Service

campaign_api_call: CampaignApiCall = CampaignApiCall()
insight_api_call: InsightApiCall = InsightApiCall()

class InsightDetectSchema(BaseModel):
    model: Insight
    detect: bool
    model_config = ConfigDict(arbitrary_types_allowed=True)

InsightDetectDict: TypeAlias = dict[int, InsightDetectSchema]

class InsightCheck(Service):
    """Insight check."""
    @validate_call
    async def main(self):
        """Insight check."""
        campaign_api_result: ServiceCampaignsSchema = campaign_api_call.get_all_campaigns()
        campaign_ids: set[int] = set()
        for campaign in campaign_api_result:
            campaign_ids.add(campaign.service_campaign_id)
        insight_api_result: InsightsSchema = []
        for campaign_id in campaign_ids:
            insight_api_result + insight_api_call.get_all_insights(campaign_id=campaign_id)
        async with database_session_manager.get_session() as session:
            session: AsyncSession
            query_result = await session.execute(select(Insight))
            database_insights = query_result.scalars().all()
            detect_insight: InsightDetectDict = {}
            for insight in database_insights:
                detect_insight[insight.id] = InsightDetectSchema(
                    model=insight,
                    detect=True,
                )
            for insight1 in insight_api_result:
                if not detect_insight[insight1.id]:
                    new_insight = Insight(
                        id=insight1.id,
                        impressions=insight1.impressions,
                        cpi=insight1.cpi,
                        ctr=insight1.ctr,
                        cpm=insight1.cpm,
                        ipm=insight1.ipm,
                        campaign_creative_id=insight1.campaign_creative_id,
                    )
                    session.add(new_insight)
                else:
                    detect_insight[insight1.id].detect = False
            deleted_insight_ids: set[int] = set()
            for value in detect_insight.values():
                if value.detect:
                    deleted_insight_ids.add(value.model.id)
            await session.execute(
                delete(Insight)
                .filter(Insight.id.in_(deleted_insight_ids))
            )
            await session.commit()


