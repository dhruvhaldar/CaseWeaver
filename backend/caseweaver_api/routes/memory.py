from fastapi import APIRouter
from pydantic import BaseModel
from caseweaver_api.dependencies import store

router = APIRouter(prefix="/api/memory", tags=["memory"])

class ImportBody(BaseModel):
    case_path: str
    summary: str = ""

@router.post("/import")
def import_case(payload: ImportBody):
    case_id = store.import_case(payload.case_path, payload.summary)
    return {"id": case_id, "status": "imported"}

@router.get("/cases")
def list_cases():
    return {"cases": store.list_cases()}
