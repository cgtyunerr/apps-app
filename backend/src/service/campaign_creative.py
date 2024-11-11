"""Campaign creative service."""
from pydantic import InstanceOf, validate_call
from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from .service import Service
from src.core import NotFoundError
from src.domain import CampaignCreativeApiCall
from src.model import CampaignCreative
from src.schema import(
    ServiceCampaignCreativesSchema,
    ServiceCampaignCreativeSchema
)


campaign_creative_api_call: CampaignCreativeApiCall = CampaignCreativeApiCall()

class CampaignCreativeService(Service):
    """Campaign creative service.

    Methods:
        get_campaign_creatives: Get all campaign creatives that are related to the campaign.
        assign_campaign_creative: Assign campaign creative to the campaign.
        unassign_campaign_creative: Unassign campaign creative from the campaign.
    """
    @validate_call
    async def get_campaign_creatives(
        self,
        session: InstanceOf[AsyncSession],
        campaign_id: int,
    ) -> ServiceCampaignCreativesSchema:
        """Get all campaign creatives that are related to the campaign.

        Arguments:
            session: Database session.
            campaign_id: ID of the campaign.

        Returns:
            DatabaseCampaignCreativesSchema.

        Raises:
            NotFoundError: If the campaign creative does not exist.
        """

        query_result = await session.execute(select(CampaignCreative)
                                             .filter(CampaignCreative.campaign_id == campaign_id))
        campaign_creatives = query_result.scalars().all()
        result: ServiceCampaignCreativesSchema = []
        for campaign_creative in campaign_creatives:
            result.append(
                ServiceCampaignCreativeSchema(
                    id=campaign_creative.id,
                    status=campaign_creative.status,
                    created_at=campaign_creative.created_at,
                    asset_id=campaign_creative.asset_id,
                )
            )

        if len(result) == 0:
            raise NotFoundError
        return result

    @validate_call
    async def assign_campaign_creative(
        self,
        session: InstanceOf[AsyncSession],
        campaign_id: int,
        asset_ids: list[int],
    ) -> ServiceCampaignCreativesSchema:
        """Assign campaign creative to the campaign.

        Arguments:
            session: Database session.
            campaign_id: ID of the campaign.
            asset_ids: Asset ids to assign the campaign.

        Returns:
            ServiceCampaignCreativesSchema.
        """
        result: ServiceCampaignCreativesSchema = campaign_creative_api_call.assign_campaign_creative(
            campaign_id=campaign_id,
            asset_ids=asset_ids,
        )
        if len(result) == 0:
            raise NotFoundError

        new_campaign_creative: list[CampaignCreative] = []
        for campaign_creative in result:
            new_campaign_creative.append(
                CampaignCreative(
                    id=campaign_creative.id,
                    status=campaign_creative.status,
                    created_at=campaign_creative.created_at,
                    asset_id=campaign_creative.asset_id,
                    campaign_id=campaign_id,
                )
            )
        session.add_all(new_campaign_creative)
        await session.commit()
        return result

    @validate_call
    async def unassign_campaign_creative(
        self,
        session: InstanceOf[AsyncSession],
        campaign_id: int,
        creative_ids: list[int],
    ) -> None:
        """Unassign campaign creative from the campaign.

        Arguments:
            session: Database session.
            campaign_id: ID of the campaign.
            creative_ids: Asset ids to unassign the campaign.

        Return:
            None.
        """
        campaign_creative_api_call.unassign_campaign_creative(
            campaign_id=campaign_id,
            creative_ids=creative_ids,
        )
        await session.execute(
            delete(CampaignCreative)
            .filter(CampaignCreative.campaign_id == campaign_id)
            .filter(CampaignCreative.id.in_(creative_ids))
        )


