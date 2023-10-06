from sqlalchemy import String, UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.setup import Base
from app.core.utils import new_uuid


class Team(Base):
    __tablename__ = 'teams'

    id: Mapped[str] = mapped_column(UUID(as_uuid=True), primary_key=True,
                                    default=new_uuid, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String)
    # players: Mapped[List["Player"]] = relationship(back_populates="team")
