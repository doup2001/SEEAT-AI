from sqlalchemy.orm import Session, joinedload
from app.models.review import Review

def get_all_reviews(db: Session) -> list[Review]:
    """
    DB에서 모든 Review 객체와 연관된 해시태그 리스트까지 함께 조회합니다.
    """
    return db.query(Review).options(joinedload(Review.hashtags)).all()
