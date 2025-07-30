"""
DB 세션 유틸리티 모듈

SessionLocal 객체를 생성하여 전체 애플리케이션에서 DB 세션을 손쉽게 가져올 수 있도록 합니다.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy.engine import Engine

load_dotenv()

# ENV 에서 주소값 가져오기
MYSQL_ADDRESS = os.getenv("MYSQL_ADDRESS")
if not MYSQL_ADDRESS:
    raise ValueError("환경 변수 MYSQL_ADDRESS가 설정되어 있지 않습니다.")

# SQLAlchemy 엔진 생성
engine: Engine = create_engine(
    MYSQL_ADDRESS,
    echo=False,            # echo=True는 디버깅용, 운영에선 False 권장
    pool_pre_ping=True,    # 연결이 끊긴 커넥션 자동 복구
    pool_recycle=1800      # 오래된 연결 자동 재생성 (30분)
)

# 세션 팩토리 생성
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
