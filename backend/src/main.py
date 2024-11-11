"""Main project file."""
from fastapi import FastAPI

from src.api import asset_router, campaign_router, campaign_creative_router
from src.middleware import ErrorHandlerMiddleware

app = FastAPI(
    title="Backend",
    description="Apps app backend",
    version="1.0.0",
)

app.add_middleware(ErrorHandlerMiddleware)
app.include_router(asset_router)
app.include_router(campaign_router)
app.include_router(campaign_creative_router)
