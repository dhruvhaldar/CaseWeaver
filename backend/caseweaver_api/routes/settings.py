from fastapi import APIRouter
router = APIRouter(prefix="/api/settings", tags=["settings"])
@router.get("/")
def settings():
    return {"model": "Qwen2.5-7B-Instruct", "local_first": True}
