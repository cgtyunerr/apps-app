"""Insight ORM model."""
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixin import integer, real

class Insight(Base):
    """Insight model."""
    __tablename__ = 'insight'

    impressions: Mapped[integer]
    cpi: Mapped[real]
    ctr: Mapped[real]
    cpm: Mapped[real]
    ipm: Mapped[real]
    campaign_creative_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('campaign_creative.id'), nullable=False
    )