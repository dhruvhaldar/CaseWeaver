from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from caseweaver_core.solvers.openfoam.manager import detect_openfoam

router = APIRouter(prefix="/api/openfoam", tags=["openfoam"])

@router.get("/detect")
def detect():
    return detect_openfoam()

@router.get("/updates")
def updates():
    return {
        "openfoam_versions": {
            "foundation": [{"version": "13", "package": "openfoam13", "release_date": "2025-07-08"}],
            "opencfd": [{"version": "v2512", "package": "openfoam2512", "release_date": "2025-12-22"}],
        }
    }

class UpdateBody(BaseModel):
    confirm: bool = False

@router.post("/update")
def update(body: UpdateBody):
    if not body.confirm:
        raise HTTPException(status_code=400, detail="Explicit confirmation required")
    return {"status": "planned_only", "message": "No privileged command executed in MVP"}
