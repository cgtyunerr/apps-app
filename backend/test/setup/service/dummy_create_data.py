"""Dummy data creation for tests."""
from datetime import datetime

from src.database import database_session_manager
from src.model import Asset

class CreateData:
    """Create dummy data."""
    @staticmethod
    async def create_dummy_data():
        """Create dummy data for tests."""
        new_assets: set[Asset] = {
            Asset(
                id=100000,
                service_asset_id=100,
                title="asset1",
                status="eligible",
                created_at=datetime(2020, 1, 1),
            ),
            Asset(
                id=100001,
                service_asset_id=101,
                title="asset2",
                status="error",
                created_at=datetime(2020, 1, 2),
            ),
            Asset(
                id=100002,
                service_asset_id=102,
                title="asset3",
                status="processing",
                created_at=datetime(2020, 1, 3),
            ),
            Asset(
                id=100003,
                service_asset_id=103,
                title="asset4",
                status="removed",
                created_at=datetime(2020, 1, 4),
            )
        }
        async with database_session_manager.get_session() as session:
            session.add_all(new_assets)
            await session.commit()