"""Asset domain unit tests."""
from io import BytesIO
from fastapi import UploadFile
from pathlib import Path
import pytest

from src.domain import AssetApiCall
from src.schema import ServiceAssetSchema, ServiceAssetsSchema

base_dir = Path(__file__).resolve().parents[3] / 'setup' / 'domain'

@pytest.fixture
def asset_api_call() -> AssetApiCall:
    """Create and return a asset api call instance."""
    return AssetApiCall()

def file_to_upload_file(file_path: str)-> UploadFile:
    path = base_dir / file_path
    with open(path, "rb") as f:
        file_content = f.read()
    file = UploadFile(filename=file_path, file=BytesIO(file_content))
    return file


class TestCreateAsset:
    """Test create asset api call."""
    def test_create_one_asset(self, asset_api_call):
        """Create one asset api call."""
        image1: UploadFile = file_to_upload_file(file_path="400x300.jpg")
        api_result: ServiceAssetsSchema = asset_api_call.create_asset(
            assets= [image1]
        )

        assert len(api_result) == 1

        for asset in api_result:
            asset_api_call.delete_asset(asset.service_asset_id)


    def test_create_many_asset(self, asset_api_call):
        """Test add multiple asset."""
        image1: UploadFile = file_to_upload_file(file_path="400x300.jpg")
        image2: UploadFile = file_to_upload_file(file_path="400x400.jpg")
        api_result: ServiceAssetsSchema = asset_api_call.create_asset(
            assets=[image1, image2]
        )

        assert len(api_result) == 2

        for asset in api_result:
            asset_api_call.delete_asset(asset.service_asset_id)


class TestGetAsset:
    """Test get asset with api call."""
    def test_get_all_assets(self, asset_api_call):
        """Test get all assets with api call."""
        image1: UploadFile = file_to_upload_file(file_path="400x300.jpg")
        image2: UploadFile = file_to_upload_file(file_path="400x400.jpg")
        temp_create: ServiceAssetsSchema = asset_api_call.create_asset(
            assets=[image1, image2]
        )
        api_result: ServiceAssetsSchema = asset_api_call.get_all_assets()
        expected_ids: set[int] = {asset.service_asset_id for asset in temp_create}
        actual_ids: set[int] = {asset.service_asset_id for asset in api_result}

        assert expected_ids.issubset(actual_ids)

        for asset_id in expected_ids:
            asset_api_call.delete_asset(asset_id)

    def test_get_one_asset(self, asset_api_call):
        """Get one asset with api call."""
        image1: UploadFile = file_to_upload_file(file_path="400x300.jpg")
        temp_create: ServiceAssetsSchema = asset_api_call.create_asset(
            assets=[image1]
        )
        api_result: ServiceAssetSchema = asset_api_call.get_asset(
            asset_id=temp_create[0].service_asset_id
        )
        assert api_result.service_asset_id == temp_create[0].service_asset_id

        asset_api_call.delete_asset(temp_create[0].service_asset_id)


class TestDeleteAsset:
    """Test delete asset with api call."""
    def test_delete_asset(self, asset_api_call):
        image1: UploadFile = file_to_upload_file(file_path="400x300.jpg")
        temp_create: ServiceAssetsSchema = asset_api_call.create_asset(
            assets=[image1]
        )
        asset_api_call.delete_asset(asset_id=temp_create[0].service_asset_id)
        all_assets: ServiceAssetsSchema = asset_api_call.get_all_assets()
        all_asset_ids: set[int] = {asset.service_asset_id for asset in all_assets}
        not_expected_asset_ids: set[int] = {temp_create[0].service_asset_id}
        assert not not_expected_asset_ids.issubset(all_asset_ids)
