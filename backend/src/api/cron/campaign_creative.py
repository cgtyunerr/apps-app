"""Campaign creative cron job api."""
from src.service import CampaignCreativeService

campaign_creative_status_checker: CampaignCreativeService = CampaignCreativeService()

async def check_campaign_creative_status():
    """Check asset status."""
    await campaign_creative_status_checker.main()