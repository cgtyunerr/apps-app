"""Campaign Creative ORM model."""
from sqlalchemy import UniqueConstraint, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixin import text

class CampaignCreative(Base):
    """Campaign Creative model."""
    __tablename__ = 'campaign_creative'

    status: Mapped[text]
    campaign_id: Mapped[int] = mapped_column(
        Integer, nullable=False
    )
    asset_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('asset.id'), nullable=False
    )

    __table_args__ = (UniqueConstraint('campaign_id', 'asset_id'),)
