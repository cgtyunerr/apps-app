"""Campaign creative cron job api."""
from src.service import CampaignCreativeStatusChecker

campaign_creative_status_checker: CampaignCreativeStatusChecker = CampaignCreativeStatusChecker()

async def check_campaign_creative_status():
    """Check asset status."""
    await campaign_creative_status_checker.main()