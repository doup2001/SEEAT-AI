from langchain.schema import Document

def db_reviews_to_documents(reviews: list) -> list:
    """
    DB에서 조회한 리뷰 리스트를 LangChain Document 리스트로 변환합니다.

    Args:
        reviews (list): DB에서 조회한 리뷰 ORM 객체 리스트

    Returns:
        list: LangChain Document 객체 리스트
    """
    documents = []
    for review in reviews:
        content = f"""
        작성자 ID: {review.user_id}
        영화관 좌석 ID: {review.seat_id}
        영화 제목: {review.movie_title}
        후기 내용: {review.content}
        평점: {review.rating}점
        썸네일 URL: {review.thumbnail_url if review.thumbnail_url else '없음'}
        생성일: {review.created_at}
        수정일: {review.updated_at}
        """
        documents.append(Document(page_content=content.strip()))
    return documents
