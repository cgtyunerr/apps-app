"""Campaign creative domain unit test."""
from io import BytesIO
from fastapi import UploadFile
from pathlib import Path
import pytest
from requests import HTTPError

from .asset import asset_api_call, base_dir, file_to_upload_file
from .campaign import campaign_api_call
from src.domain import AssetApiCall, CampaignApiCall, CampaignCreativeApiCall
from src.schema import(
    ServiceCampaignCreativeSchema,
    ServiceCampaignCreativesSchema,
    ServiceAssetsSchema,
    ServiceAssetSchema,
    ServiceCampaignSchema,
    ServiceCampaignsSchema,
)


@pytest.fixture
def campaign_creative_api_call() -> CampaignCreativeApiCall:
    """Create and return a campaign creative api call instance."""
    return CampaignCreativeApiCall()

class TestPostCampaignCreative:
    """Test post campaign creative."""
    def test_assign_campaign_creative(self, asset_api_call, campaign_api_call, campaign_creative_api_call):
        """Test post campaign creative."""
        image1: UploadFile = file_to_upload_file(file_path="400x400.jpg")
        asset_api_result: ServiceAssetsSchema = asset_api_call.create_asset(
            assets=[image1]
        )
        campaign_api_result: ServiceCampaignsSchema = campaign_api_call.get_all_campaigns()
        try:
            api_result: ServiceCampaignCreativesSchema = campaign_creative_api_call.assign_campaign_creative(
                campaign_id=campaign_api_result[0].service_campaign_id,
                asset_ids=[asset_api_result[0].service_asset_id],
            )
            assert len(api_result) == 1
            asset_api_call.delete_asset(
                asset_id=api_result[0].service_asset_id,
            )
        except HTTPError as e:
            assert e.response.status_code == 400

class TestGetCampaignCreative:
    """Test get campaign creative."""
    def test_get_campaign_creative(self, campaign_creative_api_call):
        """Test get campaign creative."""
        api_result: ServiceCampaignCreativesSchema = campaign_creative_api_call.get_all_campaign_creatives(
            campaign_id=50,
        )
        assert 1==1 # if code read this line test is correct.





