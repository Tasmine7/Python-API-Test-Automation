from logger_config import logger


def test_update_user(api_client):

    logger.info("Starting PUT test")

    payload = {
        "name": "Tas Updated",
        "username": "tas_updated",
        "email": "updated@example.com"
    }

    response = api_client.put("/users/1", payload)

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Tas Updated"
    assert data["email"] == "updated@example.com"

    logger.info("PUT test passed")