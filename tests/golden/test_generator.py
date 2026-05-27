from caseweaver_core.schemas.casespec import CaseSpec
from caseweaver_core.generation.openfoam_generator import generate_lid_driven_cavity


def test_lid_driven_cavity_golden_strings():
    files = generate_lid_driven_cavity(CaseSpec(reynolds_number=100))
    assert "application icoFoam" in files["system/controlDict"]
    assert "(50 50 1)" in files["system/blockMeshDict"]
