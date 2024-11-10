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

    def get(self, path, arguments: dict|None) -> dict|list:
        """Define get request."""
        if arguments is None:
            result: Response = requests.get(settings.BASE_URL + path,
                                            headers={"Authorization": "Bearer " + settings.TOKEN})
            result.raise_for_status()
            return result.json()
        else:
            result: Response = requests.get(settings.BASE_URL + path,
                                            headers={"Authorization": "Bearer " + settings.TOKEN},
                                            params=arguments)
            result.raise_for_status()
            return result.json()


    def post(self, path, body: dict|None, files: list|None) -> dict|list:
        if body:
            result: Response = requests.post(settings.BASE_URL + path,
                                             headers={"Authorization": "Bearer "+settings.TOKEN}, json=body)
            result.raise_for_status()
            return result.json()
        elif files:
            result: Response = requests.post(settings.BASE_URL + path,
                                             headers={"Authorization": "Bearer "+settings.TOKEN,
                                                      "accept": "application/json"},
                                             files=files)
            result.raise_for_status()
            return result.json()


    def put(self, path, body: dict) -> dict:
        result: Response = requests.put(settings.BASE_URL + path,
                                        headers={"Authorization": "Bearer "+settings.TOKEN}, json=body)
        result.raise_for_status()
        return result.json()


    def delete(self, path) -> None:
        result: Response = requests.delete(settings.BASE_URL + path, headers={"Authorization": "Bearer "+settings.TOKEN},)
        result.raise_for_status()


