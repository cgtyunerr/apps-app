"""Campaign api call module."""
from pydantic import validate_call

from .api_call import ApiCall
from src.schema import ServiceCampaignsSchema, ServiceCampaignSchema

class CampaignApiCall(ApiCall):
    """Campaign api call class.

    Methods:
        get_all_campaigns: get all campaigns.
        get_campaign: get campaign.
        update_campaign: update campaign.
    """

    @validate_call
    def get_all_campaigns(self) -> ServiceCampaignsSchema:
        """Get all campaigns.

        Arguments:
            None.
        Returns:
            All the campaigns.
        """
        api_result: list = self.api_call.get(
            path="/campaign/all",
            arguments=None,
        )
        result: ServiceCampaignsSchema = []
        for campaign in api_result:
            result.append(ServiceCampaignSchema(
                service_campaign_id=campaign["id"],
                title=campaign["title"],
                created_at=campaign["created_at"],
                active=campaign["active"],
            ))

        return result

    @validate_call
    def get_campaign(self, campaign_id: int) -> ServiceCampaignSchema:
        """Get campaign.

        Arguments:
            campaign_id: campaign id.

        Returns:
            The campaign.
        """
        api_result: dict = self.api_call.get(
            path="/campaign/{}".format(campaign_id),
            arguments=None,
        )
        return ServiceCampaignSchema(
            service_campaign_id=api_result["id"],
            title=api_result["title"],
            created_at=api_result["created_at"],
            active=api_result["active"],
        )

    @validate_call
    def update_campaign(self, campaign_id: int, active: bool) -> None:
        """Update campaign.

        Arguments:
            campaign_id: campaign id.
            active: whether campaign is active.
        Returns:
            None.
        """
        self.api_call.put(
            path="/campaign/{}".format(campaign_id),
            body={"campaign_id": campaign_id ,"active": active},
        )
