"""Celery tasks."""
import asyncio

from celery.app import Celery
from celery.schedules import crontab

from src import settings
from src.api import check_asset_status, check_campaign_creative_status, check_insight

celery: Celery = Celery(
    "celery-app",
    broker=f"redis://{settings.REDIS.HOST}:{settings.REDIS.PORT}/0",
)

@celery.task
def check_asset():
    """Check asset status."""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check_asset_status())

@celery.task
def check_campaign_creative():
    """Check campaign creative status."""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check_campaign_creative_status())

@celery.task
def check_insights():
    """Check Insights."""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check_insight())

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """setup periodic tasks."""
    sender.add_periodic_task(
        crontab(minute="*"),
        check_asset.s(),
        name="Check asset status.",
    )
    sender.add_periodic_task(
        crontab(minute="*/2"),
        check_campaign_creative.s(),
        name="Check campaign creative status.",
    )
    sender.add_periodic_task(
        crontab(minute="*/5"),
        check_insights.s(),
        name="Check insights.",
    )
