"""Campaign create checker."""
from pydantic import InstanceOf, validate_call
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import database_session_manager
from src.domain import CampaignCreativeApiCall
from src.model import CampaignCreative
from src.schema import ServiceCampaignCreativesSchema
from .service import Service

campaign_creative_api_call: CampaignCreativeApiCall = CampaignCreativeApiCall()

class CampaignCreativeStatusChecker(Service):
    """Campaign creative checker."""

    @validate_call
    async def main(self):
        """Campaign creative checker."""
        async with database_session_manager.get_session() as session:
            session: AsyncSession
            query_result = await self._get_campaign_creative(session=session)

            campaigns_set: set[int] = set()
            for campaign_creative in query_result:
                campaigns_set.add(campaign_creative.campaign_id)

            server_campaign_creatives: ServiceCampaignCreativesSchema = []
            for campaign_id in campaigns_set:
                server_campaign_creatives = server_campaign_creatives + campaign_creative_api_call.get_all_campaign_creatives(campaign_id)

            status_schema: dict[int, str] = {}
            for campaign_creative in server_campaign_creatives:
                status_schema[campaign_creative.id] = campaign_creative.status

            for campaign_creative in query_result:
                if status_schema[campaign_creative.id] and status_schema[campaign_creative.id] != campaign_creative.status:
                    campaign_creative.status = status_schema[campaign_creative.id]
            await session.commit()



    @validate_call
    async def _get_campaign_creative(
        self,
        session: InstanceOf[AsyncSession],
    ) -> list[CampaignCreative]:
        """Get all campaign creatives.

        Arguments:
            session: database session.
        Returns:
            list[CampaignCreative].
        """
        query_result = await session.execute(
            select(CampaignCreative)
        )
        campaign_creatives = query_result.scalars().all()
        result: list[CampaignCreative] = []
        for row in campaign_creatives:
            result.append(row)
        return result
