# app/models/seat.py

from sqlalchemy import Column, String, BigInteger
from app.models.base import Base
from sqlalchemy.orm import relationship

class Seat(Base):
    __tablename__ = "seat"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    auditorium_id = Column(String(100), nullable=False)

    review_seats = relationship("ReviewSeat", back_populates="seat", cascade="all, delete-orphan")


    reviews = relationship(
        "Review",
        secondary="review_seat",
        back_populates="seats",
        lazy="joined"
    )