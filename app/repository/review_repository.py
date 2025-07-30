from sqlalchemy.orm import Session
from app.models.review import Review

def get_all_reviews(db: Session) -> list[Review]:
    return db.query(Review).all()

def get_review_by_id(db: Session, review_id: int) -> Review | None:
    return db.query(Review).filter(Review.id == review_id).first()
