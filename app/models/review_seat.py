# app/models/review_seat.py


from sqlalchemy import Column, String, Float,BigInteger, DateTime
from app.models.base import Base
from sqlalchemy.orm import relationship

class ReviewSeat(Base):
    __tablename__ = "review_seat"  # 테이블명 정확히 지정

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    seat_id = Column(String(255), index=True)
    review_id = Column(BigInteger, index=True)

    review = relationship("Review", back_populates="review_seats")
    seat = relationship("Seat", back_populates="review_seats")