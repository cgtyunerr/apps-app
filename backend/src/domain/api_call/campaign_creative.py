"""Campaign creative api call module."""
from pydantic import validate_call

from .api_call import ApiCall
from src.schema import ServiceCampaignCreativesSchema, ServiceCampaignCreativeSchema

class CampaignCreativeApiCall(ApiCall):
    """Campaign creative api call class.

    Methods:
        get_all_campaign_creatives: get all campaign creatives that related to the campaign.
        assign_campaign_creative: assign to assets and the campaign.
        unassign_campaign_creative: unassign the campaign.
    """

    @validate_call
    def get_all_campaign_creatives(self, campaign_id: int) -> ServiceCampaignCreativesSchema:
        """Get all campaign creatives that related to the campaign.
        Arguments:
            campaign_id: campaign id.
        Returns:
            ServiceCampaignCreativesSchema.
        """
        api_result: list = self.api_call.get(
            path="/campaign-creative/all",
            arguments={"campaign_id": campaign_id},
        )
        result: ServiceCampaignCreativesSchema = []
        for campaign_creative in api_result:
            result.append(ServiceCampaignCreativeSchema(
                id=campaign_creative["id"],
                status=campaign_creative["status"],
                created_at=campaign_creative["created_at"],
                asset_id=campaign_creative["asset_id"],
            ))
        return result

    @validate_call
    def assign_campaign_creative(self, campaign_id: int, asset_ids: list[int]) -> ServiceCampaignCreativesSchema:
        """Assign assets and the campaign.
        Arguments:
            campaign_id: campaign id.
            asset_ids: list of asset ids.
        Returns:
            ServiceCampaignCreativesSchema.
        """

        api_result: list = self.api_call.post(
            path="/campaign-creative/assign",
            body={"campaign_id": campaign_id, "asset_ids": asset_ids},
            files=None,
        )
        result: ServiceCampaignCreativesSchema = []
        for campaign_creative in api_result:
            result.append(ServiceCampaignCreativeSchema(
                id=campaign_creative["id"],
                created_at=campaign_creative["created_at"],
                asset_id=campaign_creative["asset_id"],
                status=campaign_creative["status"],
            ))

        return result

    @validate_call
    def unassign_campaign_creative(self, campaign_id: int, creative_ids: list[int]) -> None:
        """Unassign the campaign.
        Arguments:
            campaign_id: campaign id.
            creative_ids: list of creative ids.
        Returns:
            None.
        """
        self.api_call.post(
            path="/campaign-creative/unassign",
            body={"campaign_id": campaign_id, "creative_ids": creative_ids},
            files=None,
        )
