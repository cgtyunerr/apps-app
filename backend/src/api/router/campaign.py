"""Campaign http router."""
from typing import Annotated

from fastapi import APIRouter, Body, Depends, Path
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel
from starlette import status

from src.schema import ServiceCampaignsSchema, ServiceCampaignSchema
from src.service import CampaignService

campaign_service = CampaignService()

campaign_router = APIRouter(
    prefix="/campaign",
    tags=["campaign"],
)

class CampaignIdPathDependency(BaseModel):
    """Asset id dependency."""
    campaign_id: int = Path(..., description="Campaign id")

class CampaignUpdateBodyDependency(BaseModel):
    campaign_id: int
    active: bool

@campaign_router.get(
    path="/all",
    summary="Get all campaigns",
    response_model=ServiceCampaignsSchema,
    status_code=status.HTTP_200_OK,
)
def get_all_campaigns():
    """Get all campaigns."""
    result: ServiceCampaignsSchema = campaign_service.get_all_campaigns()
    return ORJSONResponse(
        content=jsonable_encoder(result),
    )

@campaign_router.get(
    path="/{id}",
    summary="Get a campaign by id",
    response_model=ServiceCampaignSchema,
    status_code=status.HTTP_200_OK,
)
def get_campaign_by_id(
    campaign_id: Annotated[CampaignIdPathDependency, Depends()],
):
    """Get a campaign by id."""
    result: ServiceCampaignSchema = campaign_service.get_campaign(
        campaign_id=campaign_id.campaign_id
    )
    return ORJSONResponse(
        content=jsonable_encoder(result),
    )

@campaign_router.put(
    path="/{id}",
    summary="Update a campaign by id",
    status_code=status.HTTP_204_NO_CONTENT,
)
def update_campaign(
    campaign_id: Annotated[CampaignIdPathDependency, Depends()],
    update_body: CampaignUpdateBodyDependency = Body(...),
):
    """Update a campaign by id."""
    campaign_service.update_campaign(
        campaign_id=campaign_id.campaign_id,
        active=update_body.active
    )
