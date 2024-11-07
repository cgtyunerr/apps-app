"""Main project file."""
from fastapi import FastAPI
from fastapi.middleware import Middleware

from src.middleware import ErrorHandlerMiddleware

app = FastAPI(
    title="Backend",
    description="Apps app backend",
    version="1.0.0",
)

app.add_middleware(ErrorHandlerMiddleware)
