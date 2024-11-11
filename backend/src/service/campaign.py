"""Campaign service."""
from pydantic import validate_call

from .service import Service
from src.domain import CampaignApiCall
from src.schema import ServiceCampaignsSchema, ServiceCampaignSchema

campaign_api_call: CampaignApiCall = CampaignApiCall()

class CampaignService(Service):
    """Campaign service.

    Methods:
        get_all_campaigns: Get all campaigns.
        get_campaign: Get a campaign.
        update_campaign: Update a campaign.
    """

    @validate_call
    def get_all_campaigns(
        self,
    ) -> ServiceCampaignsSchema:
        """Get all campaigns.

        Arguments:
            No arguments.

        Returns:
            ServiceCampaignsSchema.
        """
        return campaign_api_call.get_all_campaigns()

    @validate_call
    def get_campaign(
        self,
        campaign_id: int,
    ) -> ServiceCampaignSchema:
        """Get a campaign.

        Arguments:
            campaign_id: The campaign id.

        Returns:
            ServiceCampaignSchema.
        """
        return campaign_api_call.get_campaign(campaign_id)

    @validate_call
    def update_campaign(
        self,
        campaign_id: int,
        active: bool
    ) -> None:
        """Update a campaign.

        Arguments:
            campaign_id: The campaign id.
            active: Whether the campaign is active.

        Returns:
            None.
        """
        campaign_api_call.update_campaign(campaign_id, active)
