from fastapi.testclient import TestClient

from src.app import app


def test_get_activities_returns_activity_data():
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert "Chess Club" in response.json()


def test_signup_for_activity_adds_participant():
    # Arrange
    client = TestClient(app)
    email = "teststudent@mergington.edu"

    # Act
    response = client.post(f"/activities/Chess Club/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert email in response.json()["message"]


def test_unregister_participant_removes_user_from_activity():
    # Arrange
    client = TestClient(app)
    email = "removeme@mergington.edu"
    client.post(f"/activities/Chess Club/signup?email={email}")

    # Act
    response = client.delete(f"/activities/Chess%20Club/participants/{email}")

    # Assert
    assert response.status_code == 200
    assert f"Removed {email}" in response.json()["message"]
