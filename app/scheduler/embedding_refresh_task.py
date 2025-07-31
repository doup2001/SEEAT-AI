from apscheduler.schedulers.background import BackgroundScheduler
from app.services.embedding_service import EmbeddingService
from app.services.review_service import ReviewService
from app.core.logger import get_logger
from app.core.database import SessionLocal

import os
import shutil

logger = get_logger(__name__)

# DB 세션 생성
db_session = SessionLocal()

# 임베딩 서비스 및 리뷰 서비스 인스턴스 생성
embedding_service = EmbeddingService()
review_service = ReviewService(db_session)

def refresh_embedding_index():
    """
    임베딩 인덱스를 새로 생성하는 작업을 수행합니다.
    기존 인덱스가 있으면 삭제하고, 리뷰 데이터를 불러와서 인덱스를 생성한 뒤 저장합니다.
    """
    index_path = embedding_service.index_path

    # 기존 인덱스 경로가 존재하면 삭제 (재생성을 위해)
    if os.path.exists(index_path):
        shutil.rmtree(index_path)
        logger.info(f"[임베딩 갱신] 기존 인덱스 삭제 완료: {index_path}")

    # DB에서 리뷰 문서 리스트를 조회
    documents = review_service.get_review_documents()

    # 리뷰 문서가 없으면 작업을 중단하고 로그 남김
    if not documents:
        logger.warning("[임베딩 갱신] 리뷰 문서가 없어 작업을 생략합니다.")
        return

    # 새 인덱스 생성
    embedding_service.create_index(documents)

    # 인덱스를 영구 저장
    embedding_service.save_index()

    logger.info("[임베딩 갱신] FAISS 인덱스 재생성 완료")

def start_scheduler():
    """
    백그라운드 스케줄러를 시작하여 7일 간격으로 임베딩 갱신 작업을 자동 실행합니다.
    """
    scheduler = BackgroundScheduler()

    # 7일마다 refresh_embedding_index 함수 실행 예약
    scheduler.add_job(refresh_embedding_index, 'interval', days=7)

    # 스케줄러 시작 (데몬 스레드로 백그라운드에서 동작)
    scheduler.start()

    logger.info("[스케줄러] 임베딩 갱신 스케줄러 시작됨")
