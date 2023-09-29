from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.setup import Base


class Team(Base):
    __tablename__ = 'teams'

    id: Mapped[str] = mapped_column(String(16), primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String)
    # players: Mapped[List["Player"]] = relationship(back_populates="team")
