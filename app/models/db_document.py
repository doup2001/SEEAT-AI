# app/models/db_document.py

from langchain.schema import Document
from app.models.review import Review

def db_reviews_to_documents(reviews: list[Review]) -> list[Document]:
    documents = []
    for review in reviews:
        hashtags = [tag.name for tag in review.hashtags]  # 리뷰 객체에서 연결된 해시태그 추출
        content = f"""
        영화: {review.movie_title}
        좌석: {review.seat_id}
        평점: {review.rating}
        후기: {review.content}
        해시태그: {" ".join(hashtags)}
        """
        documents.append(Document(page_content=content.strip()))
    return documents
