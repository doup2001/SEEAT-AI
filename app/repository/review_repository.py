# app/repository/review_repository.py

from typing import Type
from sqlalchemy.orm import Session, joinedload
from app.models.review import Review

def get_all_reviews(db: Session) -> list[Type[Review]]:
    """
    DB에서 모든 Review 객체와 연관된 해시태그 및 좌석 정보를 함께 조회합니다.
    """
    return (
        db.query(Review)
        .options(
            joinedload(Review.hashtags),    # 해시태그 정보 즉시 로딩
            joinedload(Review.seats)              # 좌석 정보 즉시 로딩
        )
        .all()
    )
