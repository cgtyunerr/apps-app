"""Base model for SqlAlchemy."""

from .mixin import IdMixin, CreatedAtMixin
from sqlalchemy.orm import as_declarative


@as_declarative()
class Base(IdMixin, CreatedAtMixin):
    """Base class for all SQLAlchemy models."""
