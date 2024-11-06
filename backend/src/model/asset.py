"""Asset ORM model."""
from sqlalchemy.orm import Mapped

from .base import Base
from .mixin import text, unique_int

class Asset(Base):
    """Asset model."""
    __tablename__ = 'asset'

    service_asset_id: Mapped[unique_int]
    title: Mapped[text]
    status: Mapped[text]
