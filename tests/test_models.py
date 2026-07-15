def test_models(client):

    response = client.get("/models")

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True