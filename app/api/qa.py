from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.services.qa_service import QAService
from app.services.embedding_service import EmbeddingService
from app.services.review_service import ReviewService
from app.services.embedding_initializer import initialize_embeddings
from app.core.database import SessionLocal

router = APIRouter()

class QARequest(BaseModel):
    request: str = Field(..., example="상영관 ID가 13018인 리뷰들에 대해서 요약해줘")

class QAResponse(BaseModel):
    answer: str

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
    response = qa_service.query(request.request)
    return QAResponse(answer=response)
