from logger_config import logger


def test_create_user(api_client):

    logger.info("Starting POST test")

    payload = {
        "name": "Tas",
        "username": "tas123",
        "email": "tas@example.com"
    }

    response = api_client.post("/users", payload)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Tas"
    assert data["username"] == "tas123"

    logger.info("POST test passed")