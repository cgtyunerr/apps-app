"""Asset service unit test."""
import pytest

from src.database import database_session_manager
from src.schema import DatabaseAssetsSchema, DatabaseAssetSchema
from src.service.asset import AssetService

@pytest.fixture
def asset_service() -> AssetService:
    """Create and return asset service instance."""
    return AssetService()

class TestGetAssets:
    """Test get assets."""
    @pytest.mark.asyncio
    async def test_get_assets(self, asset_service: AssetService):
        """Test get assets."""
        async with database_session_manager.get_session() as session:
            result: DatabaseAssetsSchema = await asset_service.get_all_assets(session)
            result_set: set[int] = {asset.id for asset in result}
            assert result_set == set(range(100000, 100004))

    @pytest.mark.asyncio
    async def test_get_assets_by_id(self, asset_service: AssetService):
        """Test get assets by id."""
        async with database_session_manager.get_session() as session:
            result: DatabaseAssetSchema = await asset_service.get_asset(
                asset_id=100000,
                session=session
            )
            assert result.service_asset_id == 100
