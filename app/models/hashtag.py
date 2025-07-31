# app/models/hashtag.py

from sqlalchemy import Column, String, BigInteger
from app.models.base import Base
from sqlalchemy.orm import relationship

class HashTag(Base):
    __tablename__ = "hash_tag"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    review_hashtags = relationship("ReviewHashTag", back_populates="hashtag", cascade="all, delete-orphan")

    reviews = relationship(
        "Review",
        secondary="review_hash_tag",
        back_populates="hashtags",
        lazy="joined"
    )