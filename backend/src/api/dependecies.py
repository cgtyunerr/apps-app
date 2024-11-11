"""Shared dependencies for api."""
from typing import AsyncGenerator, Annotated

from fastapi import Depends, Query
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import database_session_manager


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Get a database session."""
    async with database_session_manager.get_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]

class CampaignIdQueryDependency(BaseModel):
    """Campaign creative query dependency."""
    campaign_id: int = Field(
        Query(..., description="Campaign id.")
    )
