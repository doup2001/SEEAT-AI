"""
설정 및 환경변수 로드 모듈
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ENV 에서 주소값 가져오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("환경 변수 OPENAI_API_KEY가 설정되어 있지 않습니다.")
