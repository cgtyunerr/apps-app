"""Insight domain unit test."""
import pytest

from src.domain import InsightApiCall


@pytest.fixture
def insight_api_call() -> InsightApiCall:
    """Create and return a insight api call instance."""
    return InsightApiCall()


class TestGetInsights:
    """Test get insights."""
    def test_get_insights(self, insight_api_call):
        """Test get insights."""
        api_result = insight_api_call.get_all_insights(
            campaign_id=50
        )
