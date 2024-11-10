"""Asset schemas."""
from datetime import datetime
from typing import TypeAlias

from pydantic import BaseModel

class ServiceAssetSchema(BaseModel):
    """Asset model.

    Attributes:
        service_asset_id: asset id in the service.
        title: asset title.
        status: asset status.
        created_at: asset creation date.
    """
    service_asset_id: int
    title: str
    status: str
    created_at: datetime

ServiceAssetsSchema: TypeAlias = list[ServiceAssetSchema]

class DatabaseAssetSchema(ServiceAssetSchema):
    """Asset model.

    Attributes:
        id: asset id.
    """
    id: int

DatabaseAssetsSchema: TypeAlias = list[DatabaseAssetSchema]
