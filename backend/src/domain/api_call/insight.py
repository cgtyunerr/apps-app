"""Insight api call module."""
from pydantic import validate_call

from .api_call import ApiCall
from src.schema import InsightSchema, InsightsSchema

class InsightApiCall(ApiCall):
    """Insight api call class.
    Methods:
        get_all_insights: Get all insights that is related to the campaign.
    """

    @validate_call
    def get_all_insights(self, campaign_id: int) -> InsightsSchema:
        """Get all insights that is related to the campaign.
        Arguments:
            campaign_id: campaign id.
        Returns:
            InsightsSchema.
        """
        api_result: list = self.api_call.get(
            path="/insight/all",
            arguments={"campaign_id": campaign_id},
        )
        result: InsightsSchema = []
        for insight in api_result:
            result.append(InsightSchema(
                id=insight["id"],
                campaign_creative_id=insight["creative_id"],
                created_at=insight["created_at"],
                impressions=insight["impressions"],
                cpi=insight["cpi"],
                ctr=insight["ctr"],
                cpm=insight["cpm"],
                imp=insight["imp"],
            ))

        return result
