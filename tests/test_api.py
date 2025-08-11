from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

DUMMY_AUDIO = __file__

def test_detect_language_endpoint():
    response = client.post("/detect/language", json={
        "audio_file_path": DUMMY_AUDIO,
        "ground_truth_language": "en"
    })
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert isinstance(data["results"], list)
    assert len(data["results"]) == 4
    for result in data["results"]:
        assert "provider" in result
        assert "language" in result
        assert "status" in result
