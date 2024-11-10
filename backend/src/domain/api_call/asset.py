"""Asset api call module."""
from io import BytesIO
from fastapi import UploadFile
from pydantic import validate_call

from .api_call import ApiCall
from src.schema import ServiceAssetSchema, ServiceAssetsSchema

class AssetApiCall(ApiCall):
    """Asset api call class.

    Methods:
        get_all_assets: Get all assets.
        get_asset: Get the asset.
        delete_asset: Delete the asset.
        create_asset: Create a new asset.
    """

    @validate_call
    def get_all_assets(self) -> ServiceAssetsSchema:
        """Get all assets.
        Arguments:
            No arguments.
        Returns:
            All the assets.
        """
        call_result: list = self.api_call.get(
            path="/asset/all",
            arguments=None,
        )
        result: ServiceAssetsSchema = []
        for row in call_result:
            result.append(
                ServiceAssetSchema(
                    service_asset_id=row["id"],
                    title=row["title"],
                    status=row["status"],
                    created_at=row["created_at"],
                )
            )

        return result

    @validate_call
    def get_asset(self, asset_id: int) -> ServiceAssetSchema:
        """Get asset.

        Arguments:
            asset_id: The asset id.

        Returns:
            The asset.
        """
        call_result: dict = self.api_call.get(
            path="/asset/{}".format(asset_id),
            arguments=None,
        )

        return ServiceAssetSchema(
            service_asset_id=call_result["id"],
            title=call_result["title"],
            status=call_result["status"],
            created_at=call_result["created_at"],
        )

    @validate_call
    def delete_asset(self, asset_id: int) -> None:
        """Delete asset.

        Arguments:
            asset_id: The asset id.
        Return:
            No return.
        """
        self.api_call.delete(
            path="/asset/{}".format(asset_id),
        )

    def create_asset(self, assets: list[UploadFile]) -> ServiceAssetsSchema:
        """Create asset.

        Arguments:
            assets: The list of asset images.
        Returns:
            The new assets.
        """
        files = []
        for asset in assets:
            file_content = asset.file.read()
            file_tuple = (asset.filename, BytesIO(file_content), "image/jpeg")
            files.append(('assets', file_tuple))
        api_result: list = self.api_call.post(
            path="/asset/create",
            files=files,
            body=None,
        )
        result: ServiceAssetsSchema = []
        for row in api_result:
            result.append(
                ServiceAssetSchema(
                    service_asset_id=row["id"],
                    title=row["title"],
                    status=row["status"],
                    created_at=row["created_at"],
                )
            )
        return result





