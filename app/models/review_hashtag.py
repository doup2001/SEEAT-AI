# app/models/review_hashtag.py

from sqlalchemy import Column, BigInteger, DateTime, ForeignKey
from app.models.base import Base
from sqlalchemy.orm import relationship

class ReviewHashTag(Base):
    __tablename__ = "review_hash_tag"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    review_id = Column(BigInteger, ForeignKey("review.id"))
    hashtag_id = Column(BigInteger, ForeignKey("hash_tag.id"))

    review = relationship("Review", back_populates="review_hashtags")
    hashtag = relationship("HashTag", back_populates="review_hashtags")