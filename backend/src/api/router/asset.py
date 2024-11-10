"""Asset http router."""
from typing import Annotated

from fastapi import APIRouter, Depends, Path, File, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel
from starlette import status

from src.schema import DatabaseAssetsSchema, DatabaseAssetSchema
from src.service import AssetService

from ..dependecies import SessionDep

asset_router = APIRouter(
    prefix="/asset",
    tags=["asset"],
)

asset_service:AssetService = AssetService()

class AssetIdPathDependency(BaseModel):
    """Asset id dependency."""
    asset_id: int = Path(..., description="Asset id")


@asset_router.get(
    "/all/",
    summary="Get all assets",
    response_model=DatabaseAssetsSchema,
    status_code=status.HTTP_200_OK,
)
async def get_all_assets(
    session: SessionDep,
):
    """Get all assets."""
    result: DatabaseAssetsSchema = await asset_service.get_all_assets(session=session)
    return ORJSONResponse(
        content=jsonable_encoder(result),
    )

@asset_router.get(
    "/{asset_id}/",
    summary="Get a specific asset",
    response_model=DatabaseAssetSchema,
    status_code=status.HTTP_200_OK,
)
async def get_single_asset(
    session: SessionDep,
    asset_id: Annotated[AssetIdPathDependency, Depends()],
):
    """Get a specific asset."""
    result: DatabaseAssetSchema = await asset_service.get_single_asset(
        session=session, asset_id=asset_id.asset_id
    )
    return ORJSONResponse(
        content=jsonable_encoder(result),
    )

@asset_router.post(
    path="/create/",
    summary="Create a new asset",
    response_model=DatabaseAssetsSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_asset(
    session: SessionDep,
    files: list[UploadFile] = File(...)
):
    """Create a new asset."""
    result: DatabaseAssetsSchema = await asset_service.create_asset(
        session=session,
        files=files
    )
    return ORJSONResponse(
        content=jsonable_encoder(result)
    )

@asset_router.delete(
    path="/{asset_id}",
    summary="Delete a specific asset",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_asset(
    session: SessionDep,
    asset_id: Annotated[AssetIdPathDependency, Depends()],
):
    """Delete a specific asset."""
    await asset_service.delete_asset(
        session=session,
        asset_id=asset_id.asset_id,
    )
