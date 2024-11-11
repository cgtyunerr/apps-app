"""Destroy setup data."""
from datetime import datetime
from sqlalchemy import delete

from src.database import database_session_manager
from src.model import Asset

class DestroyData:
    """Destroy setup data."""
    @staticmethod
    async def destroy_data():
        """Destroy dummy data."""
        destroy_set: set[int] = {100000, 100001, 100002, 100003}

        async with database_session_manager.get_session() as session:
            await session.execute(
                delete(Asset).where(Asset.id.in_(destroy_set))
            )
            await session.commit()
