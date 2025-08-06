from fastapi import APIRouter

from app.scheduler import embedding_refresh_task

router = APIRouter()

@router.post("/initialize-index")
def initialize_index():
    try:
        embedding_refresh_task.refresh_embedding_index()
        return {"message": "FAISS index initialized successfully."}
    except Exception as e:
        return {"error": str(e)}
