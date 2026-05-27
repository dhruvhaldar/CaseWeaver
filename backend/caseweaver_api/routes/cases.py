from fastapi import APIRouter
from caseweaver_core.schemas.casespec import CaseSpec
from caseweaver_core.generation.openfoam_generator import generate_lid_driven_cavity

router = APIRouter(prefix="/api/cases", tags=["cases"])

@router.post("/generate")
def generate_case(spec: CaseSpec) -> dict:
    return {"spec": spec.model_dump(), "files": generate_lid_driven_cavity(spec)}
