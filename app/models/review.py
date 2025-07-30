from sqlalchemy import Column, String, Float,BigInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Review(Base):
    __tablename__ = "review"  # 테이블명 정확히 지정

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    content = Column(String(255))
    movie_title = Column(String(255))
    rating = Column(Float, nullable=False)
    thumbnail_url = Column(String(255))
    seat_id = Column(String(255), index=True)
    user_id = Column(BigInteger, index=True)

