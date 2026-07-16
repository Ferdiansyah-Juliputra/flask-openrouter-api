from unittest.mock import patch

@patch("app.routes.models.get_models")
def test_models(mock_get_models, client):
    mock_get_models.return_value = [
        {
            "id":"google/gemma-2-26b-4b-it:free"
        }
    ]
    response = client.get("/models")
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True