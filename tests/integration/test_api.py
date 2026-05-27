from fastapi.testclient import TestClient
from caseweaver_api.main import app

client = TestClient(app)


def test_generate_case():
    res = client.post("/api/cases/generate", json={"reynolds_number": 100})
    assert res.status_code == 200
    body = res.json()
    assert body["spec"]["template_id"] == "lid_driven_cavity"
    assert "system/controlDict" in body["files"]


def test_openfoam_update_requires_confirmation():
    res = client.post("/api/openfoam/update", json={"confirm": False})
    assert res.status_code == 400


def test_memory_import_and_list():
    res = client.post("/api/memory/import", json={"case_path": "/tmp/cavity"})
    assert res.status_code == 200
    case_id = res.json()["id"]
    assert case_id
    lst = client.get("/api/memory/cases")
    assert lst.status_code == 200
    assert any(c["id"] == case_id for c in lst.json()["cases"])
