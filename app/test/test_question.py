from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ask_question():
    response = client.post("/api/ask", json={"question": "C’est quoi un JWT ?"})
    assert response.status_code == 200
    assert "JWT" in response.json()["answer"]
