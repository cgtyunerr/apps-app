"""Common mixins."""

from datetime import datetime
from typing import Annotated

from sqlalchemy import BIGINT, Boolean, DateTime, String, REAL
from sqlalchemy.orm import Mapped, declarative_mixin, declared_attr, mapped_column


# Types
item_id = Annotated[
    int,
    mapped_column(
        BIGINT,
        primary_key=True,
        autoincrement=True,
    )
]

integer = Annotated[
    int,
    mapped_column(
        BIGINT,
        nullable=False,
    )
]

unique_int = Annotated[
    int,
    mapped_column(
        BIGINT,
        nullable=False,
        unique=True,
    )
]

real = Annotated[
    float,
    mapped_column(
        REAL,
        nullable=False,
    )
]

boolean = Annotated[bool, mapped_column(Boolean, default=True, nullable=False)]

text = Annotated[str, mapped_column(String, nullable=False)]


class IdMixin:
    """Mixin for id."""
    id: Mapped[item_id]

class IsActiveMixin:
    """Mixin for is_active."""
    is_active: Mapped[boolean]

class CreatedAtMixin:
    """Mixin for created_at."""
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

@declarative_mixin
class TableNameMixin:
    """Mixin for table_name."""
    @declared_attr
    def __tablename__(cls) -> str:
        """Generate table name."""
        return cls.__name__.lower()
