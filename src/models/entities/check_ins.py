# pylint: disable-all
from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func

class CheckIns(Base):
    __tablename__ = "check_ins"  # Corrigido o nome da tabela

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now())
    attendeeId = Column(String, ForeignKey("attendee.id"))

    def __repr__(self):
        return f"CheckIns [attendeeId={self.attendeeId}]"
