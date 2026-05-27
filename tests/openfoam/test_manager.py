from caseweaver_core.solvers.openfoam.manager import detect_openfoam


def test_detect_openfoam_shape():
    data = detect_openfoam()
    assert "status" in data
    assert "commands" in data
    assert "environment" in data
    assert "docker" in data
    assert "openfoam_images" in data["docker"]
    assert data["docker"]["status"] in {"available", "not_found"}
