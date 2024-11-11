"""Insight cron job api."""
from src.service import InsightCheck

insight_check: InsightCheck = InsightCheck()

async def check_insight():
    """Check asset status."""
    await insight_check.main()