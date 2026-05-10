from app import app

client = app.test_client()

def test_health():
    res = client.get("/api/health")
    assert res.status_code == 200
    assert res.json["status"] == "ok"

def test_students():
    res = client.get("/api/students")
    assert res.status_code == 200
    assert isinstance(res.json, list)
