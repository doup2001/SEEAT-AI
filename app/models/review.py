# app/models/review.py

from sqlalchemy import Column, String, Float,BigInteger, DateTime
from app.models.base import Base
from sqlalchemy.orm import relationship

class Review(Base):
    __tablename__ = "review"  # 테이블명 정확히 지정

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    content = Column(String(255))
    rating = Column(Float, nullable=False)
    thumbnail_url = Column(String(255))
    seat_id = Column(String(255), index=True)
    user_id = Column(BigInteger, index=True)


    # Review -> ReviewHashTag (중간테이블 연관)
    review_hashtags = relationship("ReviewHashTag", back_populates="review", cascade="all, delete-orphan")

    # Review -> HashTag (리스트로 바로 접근 가능하도록 secondary 연결)
    hashtags = relationship(
        "HashTag",
        secondary="review_hash_tag",
        back_populates="reviews",
        lazy="joined"  # 필요 시 즉시 페치
    )

    # Review -> ReviewSeat (중간테이블 연관)
    review_seats = relationship("ReviewSeat", back_populates="review", cascade="all, delete-orphan")

    # Review -> Seat (리스트로 바로 접근 가능하도록 secondary 연결)
    seats = relationship(
        "Seat",
        secondary="review_seat",
        back_populates="reviews",
        lazy="joined"  # 필요 시 즉시 페치
    )