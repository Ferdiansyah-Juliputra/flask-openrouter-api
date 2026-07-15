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