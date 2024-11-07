"""Http requests."""
import requests
from requests import Response

from .base import HttpRequest
from src.core import settings

class RequestsHttp(HttpRequest):
    """Http requests.
    Send http requests.

    methods:
        get: Get http requests.
        post: Post http requests.
        put: Put http requests.
        delete: Delete http requests.
    """

    def get(self, path, arguments: dict) -> dict:
        """Define get request."""
        result: Response = requests.get(settings.BASE_URL + path, params=arguments)
        return result.json()

    def post(self, body: dict) -> dict:
        result: Response = requests.post(settings.BASE_URL, data=body)
        return result.json()

    def put(self, path, body: dict) -> dict:
        result: Response = requests.put(settings.BASE_URL + path, data=body)
        return result.json()

    def delete(self, path) -> None:
        requests.delete(settings.BASE_URL + path)


