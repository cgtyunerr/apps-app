"""Insight http router."""
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import ORJSONResponse
from starlette import status

from src.schema import InsightsSchema
from src.service import InsightService
from ..dependecies import CampaignIdQueryDependency, SessionDep

insight_service: InsightService = InsightService()

insight_router = APIRouter(
    prefix="/insight",
    tags=["insight"],
)


@insight_router.get(
    path="/all",
    summary="Get all insights that are related to campaign",
    response_model=InsightsSchema,
    status_code=status.HTTP_200_OK,
)
async def get_insights(
    session: SessionDep,
    campaign_id: Annotated[CampaignIdQueryDependency, Depends()],
):
    result: InsightsSchema = await insight_service.get_all_insights(
        session=session,
        campaign_id=campaign_id.campaign_id,
    )
    return ORJSONResponse(
        content=jsonable_encoder(result),
    )
