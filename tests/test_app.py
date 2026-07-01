from fastapi.testclient import TestClient

from src.app import app


def test_unregister_participant_removes_user_from_activity():
    client = TestClient(app)

    response = client.delete(
        "/activities/Chess%20Club/participants/michael@mergington.edu"
    )

    assert response.status_code == 200
    data = response.json()
    assert "Removed michael@mergington.edu" in data["message"]

    activities_response = client.get("/activities")
    participants = activities_response.json()["Chess Club"]["participants"]
    assert "michael@mergington.edu" not in participants
