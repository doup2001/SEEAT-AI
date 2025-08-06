# app/services/embedding_initializer.py


from app.services.embedding_service import EmbeddingService
from app.services.review_service import ReviewService
from app.core.logger import get_logger

# 로깅
logger = get_logger(__name__)

# 인덱스가 존재하면 바로 사용하고, 없으면 새로 생성하는 함수
def initialize_embeddings(embedding_service: EmbeddingService, review_service: ReviewService):
    try:
        embedding_service.load_index()
    except Exception as e:
        logger.warning(f"인덱스 로드 실패: {e}. 인덱스 새로 생성 중...")
        documents = review_service.get_review_documents()
        if not documents:
            logger.warning("No documents to index. Please add review data.")
            return

        embedding_service.create_index(documents)
        embedding_service.save_index()