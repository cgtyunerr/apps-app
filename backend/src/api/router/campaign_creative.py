"""Campaign creative http router."""
from typing import Annotated

from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel
from starlette import status

from src.schema import ServiceCampaignCreativesSchema
from src.service import CampaignCreativeService
from ..dependecies import SessionDep, CampaignIdQueryDependency

campaign_creative_service: CampaignCreativeService = CampaignCreativeService()

campaign_creative_router = APIRouter(
    prefix="/campaign-creative",
    tags=["Campaign Creative"],
)


class AssignCampaignCreativeBodyDependency(BaseModel):
    """Assign campaign creative body dependency."""
    campaign_id: int
    asset_ids: list[int]

class UnassignCampaignCreativeBodyDependency(BaseModel):
    """Assign campaign creative body dependency."""
    campaign_id: int
    creative_ids: list[int]

@campaign_creative_router.get(
    path="/all",
    summary="Get all campaign creatives that are related to the campaign.",
    response_model=ServiceCampaignCreativesSchema,
    status_code=status.HTTP_200_OK,
)
async def get_all_campaign_creatives(
    session: SessionDep,
    campaign_id: Annotated[CampaignIdQueryDependency, Depends()],
):
    """Get all campaign creatives that are related to the campaign."""
    result: ServiceCampaignCreativesSchema = await campaign_creative_service.get_campaign_creatives(
        session=session,
        campaign_id=campaign_id.campaign_id,
    )
    return ORJSONResponse(
        content=jsonable_encoder(result),
    )

@campaign_creative_router.post(
    path="/assign",
    summary="Assign campaign creative to the campaign.",
    response_model=ServiceCampaignCreativesSchema,
    status_code=status.HTTP_200_OK,
)
async def assign_campaign_creative(
    session: SessionDep,
    assign_body: AssignCampaignCreativeBodyDependency = Body(...),
):
    """Assign campaign creative to the campaign."""
    result: ServiceCampaignCreativesSchema = await campaign_creative_service.assign_campaign_creative(
        session=session,
        campaign_id=assign_body.campaign_id,
        asset_ids=assign_body.asset_ids,
    )
    return ORJSONResponse(
        content=jsonable_encoder(result),
    )

@campaign_creative_router.post(
    path="/unassign",
    summary="Unassign campaign creative from the campaign.",
    status_code=status.HTTP_200_OK,
)
async def unassign_campaign_creative(
    session: SessionDep,
    unassign_body: UnassignCampaignCreativeBodyDependency = Body(...),
):
    """Unassign campaign creative from the campaign."""
    await campaign_creative_service.unassign_campaign_creative(
        session=session,
        campaign_id=unassign_body.campaign_id,
        creative_ids=unassign_body.creative_ids,
    )
