from fastapi import APIRouter
router = APIRouter(prefix="/api/chat", tags=["chat"])
@router.post("/")
def chat():
    return {"message": "Use /api/cases/generate with CaseSpec for deterministic generation."}
