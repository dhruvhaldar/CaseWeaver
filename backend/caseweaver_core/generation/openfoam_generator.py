from __future__ import annotations

from caseweaver_core.schemas.casespec import CaseSpec


def generate_lid_driven_cavity(spec: CaseSpec) -> dict[str, str]:
    nu = 1.0 / spec.reynolds_number
    return {
        "system/controlDict": f"application icoFoam;\\ndeltaT {spec.delta_t};\\nendTime {spec.end_time};\\n",
        "system/fvSchemes": "ddtSchemes { default Euler; }\\n",
        "system/fvSolution": "solvers { p { solver PCG; } U { solver PBiCG; } }\\n",
        "constant/transportProperties": f"nu [0 2 -1 0 0 0 0] {nu};\\n",
        "system/blockMeshDict": (
            f"convertToMeters 1;\\nblocks ((hex (0 1 2 3 4 5 6 7) ({spec.mesh_nx} {spec.mesh_ny} {spec.mesh_nz}) simpleGrading (1 1 1)));\\n"
        ),
        "0/U": "dimensions [0 1 -1 0 0 0 0];\\ninternalField uniform (0 0 0);\\n",
        "0/p": "dimensions [0 2 -2 0 0 0 0];\\ninternalField uniform 0;\\n",
    }
