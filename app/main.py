from fastapi import FastAPI
from app.api.qa import router as qa_router
from app.api.home import router as home_router
from app.api.initialize import router as init_router

app = FastAPI(title="SEEAT AI API")

# qa.py에서 만든 라우터를 앱에 등록
app.include_router(qa_router, prefix="/api/v1",)

# 홈화면 라우터를 앱에 등록
app.include_router(home_router)

# 초기화
app.include_router(init_router)
