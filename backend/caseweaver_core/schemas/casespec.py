from enum import Enum
from pydantic import BaseModel, Field


class SolverFamily(str, Enum):
    OPENFOAM = "openfoam"


class TrustLevel(str, Enum):
    UNVERIFIED = "UNVERIFIED"
    STRUCTURALLY_VALID = "STRUCTURALLY_VALID"
    MESH_VALID = "MESH_VALID"
    RUN_VALID = "RUN_VALID"
    USER_APPROVED = "USER_APPROVED"
    GOLDEN_CASE = "GOLDEN_CASE"


class CaseSpec(BaseModel):
    template_id: str = "lid_driven_cavity"
    solver_family: SolverFamily = SolverFamily.OPENFOAM
    reynolds_number: float = Field(gt=0)
    mesh_nx: int = Field(default=50, ge=10)
    mesh_ny: int = Field(default=50, ge=10)
    mesh_nz: int = Field(default=1, ge=1)
    delta_t: float = Field(default=0.001, gt=0)
    end_time: float = Field(default=10.0, gt=0)
