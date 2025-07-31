import re
from typing import List

from langchain_core.documents import Document
from app.models import Review
from app.repository.review_repository import get_all_reviews

class ReviewService:
    def __init__(self, db_session):
        """
        ReviewService 생성자

        :param db_session: SQLAlchemy DB 세션 인스턴스
        """
        self.db = db_session

    def get_review_documents(self) -> List[Document]:
        """
        DB에서 모든 Review를 조회하여 Document 리스트로 변환합니다.

        :return: Document 리스트
        """
        reviews = get_all_reviews(self.db)
        documents = self.db_reviews_to_documents(reviews)
        return documents

    @staticmethod
    def db_reviews_to_documents(reviews: List[Review]) -> List[Document]:
        """
        Review 리스트를 Document 리스트로 변환합니다.

        :param reviews: Review 객체 리스트
        :return: Document 객체 리스트
        """
        documents = []
        for review in reviews:
            hashtags = [tag.name for tag in getattr(review, 'hashtags', [])]

            # 좌석 앞자리 숫자 추출 (seat_id가 None일 경우 대비)
            seat_id = review.seat_id if review.seat_id else ""
            auditorium_id = ReviewService.extract_prefix_before_english(seat_id)

            content = (
                f"좌석: {seat_id}\n"
                f"상영관: {auditorium_id}\n"
                f"평점: {review.rating}\n"
                f"후기: {review.content}\n"
                f"해시태그: {' '.join(hashtags)}"
            )
            documents.append(Document(page_content=content.strip()))
        return documents

    @staticmethod
    def extract_prefix_before_english(s: str) -> str:
        """
        문자열에서 첫 번째 영어 알파벳이 등장하기 전까지의 숫자 부분을 추출합니다.
        영어가 없으면 원본 문자열을 그대로 반환합니다.

        :param s: 대상 문자열 (예: '13018A5')
        :return: 영어 앞의 숫자 부분 (예: '13018')
        """
        if not s:
            return ""
        match = re.match(r'^\d+', s)
        if match:
            return match.group()
        return s
