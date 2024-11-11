"""Asset status checker."""
from pydantic import validate_call
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import database_session_manager
from src.domain import AssetApiCall
from src.model import Asset
from src.schema import ServiceAssetsSchema
from .service import Service

asset_api_call: AssetApiCall = AssetApiCall()

class AssetStatusChecker(Service):
    """Asset status checker."""

    @validate_call
    async def main(self):
        """Asset status checker."""
        api_result: ServiceAssetsSchema = asset_api_call.get_all_assets()
        if len(api_result) == 0:
            return
        async with database_session_manager.get_session() as session:
            session: AsyncSession
            query_result = await session.execute(select(Asset))
            assets = query_result.scalars().all()
            result_dict: dict = {}
            for asset in api_result:
                result_dict[asset.service_asset_id] = asset.status
            for asset in assets:
                if result_dict.get(asset.service_asset_id) and result_dict[asset.service_asset_id] == asset.status:
                    asset.status = result_dict[asset.service_asset_id]

            await session.commit()

