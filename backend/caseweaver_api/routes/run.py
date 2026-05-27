from fastapi import APIRouter
router = APIRouter(prefix="/api/run", tags=["run"])
@router.post("/validate")
def validate_run():
    return {"status": "not_implemented", "detail": "Use local OpenFOAM commands in future iterations."}
