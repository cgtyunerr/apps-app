"""Http request base."""
from abc import ABC, abstractmethod

class HttpRequest(ABC):
    """Http request base class.

    This class is abstract class of http request.

    methods:
        get: http get method.
        post: http post method.
        put: http put method.
        delete: http delete method.
    """

    @abstractmethod
    def get(self, path, arguments: dict) -> dict:
        """http get method."""

    @abstractmethod
    def post(self, body: dict) -> dict:
        """http post method."""

    @abstractmethod
    def put(self, path, body: dict) -> dict:
        """http put method."""

    @abstractmethod
    def delete(self, path) -> None:
        """http delete method."""
