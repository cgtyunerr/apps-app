"""Asset cron job api."""
from src.service import AssetStatusChecker

asset_status_checker: AssetStatusChecker = AssetStatusChecker()

async def check_asset_status():
    """Check asset status."""
    await asset_status_checker.main()