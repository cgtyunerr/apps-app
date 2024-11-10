"""Api call base module."""
from pydantic import BaseModel

from .base import HttpRequest
from .http_requests import RequestsHttp

class ApiCall(BaseModel):
    """Api call base class."""
    api_call: HttpRequest = RequestsHttp()
    model_config = {
        "arbitrary_types_allowed": True
    }
