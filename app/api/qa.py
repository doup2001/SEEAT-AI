from fastapi import APIRouter
from pydantic import BaseModel

from app.services.qa_service import QAService
from app.services.embedding_service import EmbeddingService
from app.services.review_service import ReviewService
from app.services.embedding_initializer import initialize_embeddings
from app.core.database import SessionLocal

router = APIRouter()

class QARequest(BaseModel):
    query: str

class QAResponse(BaseModel):
    answer: str
    sources: list[str] = []

# DB 세션 생성
db_session = SessionLocal()

# 서비스 객체 생성
embedding_service = EmbeddingService()
review_service = ReviewService(db_session)

# 임베딩 초기화
initialize_embeddings(embedding_service, review_service)

qa_service = QAService(embedding_service.vectorstore)

@router.post("/summary", response_model=QAResponse)
def get_qa_answer(request: QARequest):
    response = qa_service.query(request.query)
    return response
