"""Campaign domain unit test"""
import pytest
from requests import HTTPError

from src.domain import CampaignApiCall
from src.schema import ServiceCampaignSchema, ServiceCampaignsSchema

@pytest.fixture
def campaign_api_call()->CampaignApiCall:
    """Create and return a campaign api call instance."""
    return CampaignApiCall()

class TestGetCampaign:
    """Get campaign test."""
    def test_get_all_campaigns(self, campaign_api_call: CampaignApiCall):
        """Test get all campaigns."""
        api_result: ServiceCampaignsSchema = campaign_api_call.get_all_campaigns()
        for campaign in api_result:
            assert isinstance(campaign, ServiceCampaignSchema)

    def test_get_campaign(self, campaign_api_call: CampaignApiCall):
        """Test get campaign."""
        api_temp: ServiceCampaignsSchema = campaign_api_call.get_all_campaigns()
        if len(api_temp) > 0:
            api_result: ServiceCampaignSchema = campaign_api_call.get_campaign(
                campaign_id=api_temp[0].service_campaign_id
            )
            assert isinstance(api_result, ServiceCampaignSchema)

class TestPutCampaign:
    """Put campaign test."""
    def test_put_campaign(self, campaign_api_call: CampaignApiCall):
        """Test put campaign."""
        api_temp: ServiceCampaignsSchema = campaign_api_call.get_all_campaigns()
        if len(api_temp) > 0:
            if api_temp[0].active:
                try:
                    campaign_api_call.update_campaign(
                        campaign_id=api_temp[0].service_campaign_id,
                        active=False
                    )
                    campaign: ServiceCampaignSchema = campaign_api_call.get_campaign(
                        campaign_id=api_temp[0].service_campaign_id
                    )
                    assert not campaign.active
                    campaign_api_call.update_campaign(
                        campaign_id=api_temp[0].service_campaign_id,
                        active=True
                    )
                except HTTPError as e:
                    assert e.response.status_code == 400
            else:
                try:
                    campaign_api_call.update_campaign(
                        campaign_id=api_temp[0].service_campaign_id,
                        active=True
                    )
                    campaign: ServiceCampaignSchema = campaign_api_call.get_campaign(
                        campaign_id=api_temp[0].service_campaign_id
                    )
                    assert campaign.active
                    campaign_api_call.update_campaign(
                        campaign_id=api_temp[0].service_campaign_id,
                        active=False
                    )
                except HTTPError as e:
                    assert e.response.status_code == 400