"""Asset schemas."""
from datetime import datetime
from typing import TypeAlias

from pydantic import BaseModel

class AssetSchema(BaseModel):
    """Asset model.

    Attributes:
        id: asset id.
        title: asset title.
        status: asset status.
        created_at: asset creation date.
    """
    id: int
    title: str
    status: str
    created_at: datetime

AssetsSchema: TypeAlias = list[AssetSchema]
