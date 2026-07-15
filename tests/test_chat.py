from unittest.mock import patch

@patch("app.routes.chat.generate_response")
def test_chat_success(mock_generate_response, client):
    mock_generate_response.return_value = "Hello from Mock!"

    response = client.post(
        "/chat",
        json={
            "message": "Hello"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True
    
    assert data["data"]["reply"] == "Hello from Mock!"
    
def test_chat_without_message(client):

    response = client.post(
        "/chat",
        json={}
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["success"] is False
    

def test_chat_empty_message(client):

    response = client.post(
        "/chat",
        json={
            "message": ""
        }
    )

    assert response.status_code == 400