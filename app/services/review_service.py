from app.repository.review_repository import get_all_reviews
from app.models.db_document import db_reviews_to_documents

class ReviewService:
    def __init__(self, db_session):
        self.db = db_session

    def get_review_documents(self):

        # 레포지토리 함수 호출
        reviews = get_all_reviews(self.db)

        # 도큐먼트로 문서 변환
        documents = db_reviews_to_documents(reviews)
        return documents
