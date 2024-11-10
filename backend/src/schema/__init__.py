"""Pydantic schema module."""
from .asset import ServiceAssetSchema, ServiceAssetsSchema, DatabaseAssetSchema, DatabaseAssetsSchema
from .campaign import ServiceCampaignsSchema, ServiceCampaignSchema
from .campaign_creative import(
    ServiceCampaignCreativeSchema,
    ServiceCampaignCreativesSchema,
    DatabaseCampaignCreativeSchema,
    DatabaseCampaignCreativesSchema,
)
from .insight import InsightSchema, InsightsSchema
__all__ = [
    # Asset
    "ServiceAssetSchema",
    "ServiceAssetsSchema",
    "DatabaseAssetSchema",
    "DatabaseAssetsSchema",
    # Campaign
    "ServiceCampaignSchema",
    "ServiceCampaignsSchema",
    # Campaign Creative
    "ServiceCampaignCreativeSchema",
    "ServiceCampaignCreativesSchema",
    "DatabaseCampaignCreativeSchema",
    "DatabaseCampaignCreativesSchema",
    # Insight
    "InsightSchema",
    "InsightsSchema",
]
