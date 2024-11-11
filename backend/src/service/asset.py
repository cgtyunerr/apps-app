"""Asset service."""
from fastapi import UploadFile
from pydantic import InstanceOf, validate_call
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .service import Service
from src.domain import AssetApiCall
from src.core import NotFoundError
from src.model import Asset
from src.schema import DatabaseAssetsSchema, DatabaseAssetSchema, ServiceAssetsSchema

asset_api_call: AssetApiCall = AssetApiCall()

class AssetService(Service):
    """Asset service.

    methods:
        get_all_assets: get all assets.
        get_asset: get a asset
        create_asset: post a new asset.
        delete: delete a asset.
    """
    @validate_call
    async def get_all_assets(
        self,
        session: InstanceOf[AsyncSession],
    ) -> DatabaseAssetsSchema:
        """Get all assets.

        Arguments:
            session: database session.

        Returns:
            Assets: all assets.

        Raises:
            NotFoundError: If asset does not exist.
        """
        query_result = await session.execute(select(Asset))
        assets = query_result.scalars().all()
        result: DatabaseAssetsSchema = []
        for asset in assets:
            result.append(
                DatabaseAssetSchema(
                    id=asset.id,
                    service_asset_id=asset.service_asset_id,
                    title=asset.title,
                    status=asset.status,
                    created_at=asset.created_at,
                )
            )
        if len(result) == 0:
            raise NotFoundError

        return result

    @validate_call
    async def get_asset(
        self,
        asset_id: int,
        session: InstanceOf[AsyncSession],
    ) -> DatabaseAssetSchema:
        """Get a asset.

        Arguments:
            asset_id: asset id.
            session: database session.
        """
        query_result = await session.execute(select(Asset).filter(Asset.id == asset_id))
        asset = query_result.scalar_one_or_none()

        if not asset:
            raise NotFoundError

        return DatabaseAssetSchema(
            id=asset.id,
            service_asset_id=asset.service_asset_id,
            title=asset.title,
            status=asset.status,
            created_at=asset.created_at
        )

    @validate_call
    async def create_asset(
        self,
        files: list[UploadFile],
        session: InstanceOf[AsyncSession],
    ) -> DatabaseAssetsSchema:
        """Post a new asset.

        Arguments:
            files: uploaded files.
            session: database session.

        Return:
            new asset.
        """
        api_result: ServiceAssetsSchema = asset_api_call.create_asset(assets=files)
        new_assets: list[Asset] = []
        for api_asset in api_result:
            new_assets.append(
                Asset(
                    service_asset_id=api_asset.id,
                    title=api_asset.title,
                    status=api_asset.status,
                    created_at=api_asset.created_at
                )
            )
        session.add_all(new_assets)
        await session.commit()
        new_db_assets: DatabaseAssetsSchema = []
        for asset in new_assets:
            new_db_assets.append(
                DatabaseAssetSchema(
                    id=asset.id,
                    service_asset_id=asset.service_asset_id,
                    title=asset.title,
                    status=asset.status,
                    created_at=asset.created_at,
                )
            )
        return new_db_assets

    @validate_call
    async def delete_asset(
        self,
        asset_id: int,
        session: InstanceOf[AsyncSession],
    ):
        """Delete a asset.

        Arguments:
            asset_id: asset id.
            session: database session.

        Return:
            None.
        """
        asset_api_call.delete_asset(asset_id=asset_id)
        query_result = await session.execute(select(Asset).filter(Asset.id == asset_id))
        asset = query_result.scalar_one_or_none()
        if not asset:
            raise NotFoundError
        await session.delete(asset)
