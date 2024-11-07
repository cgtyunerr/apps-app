"""Main project module."""
from .core import settings
from .model import Base

__all__ = [
    "Base",
    "settings",
]
