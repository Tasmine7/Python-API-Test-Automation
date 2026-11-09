import pytest
from logger_config import logger


def test_get_all_users(api_client):

    logger.info("Starting GET all users test")

    response = api_client.get("/users")

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

    logger.info("GET all users test passed")


def test_get_invalid_user(api_client):

    logger.info("Starting negative GET test")

    response = api_client.get("/users/9999")

    assert response.status_code == 404

    logger.info("Negative GET test passed")


@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_get_user_by_id(api_client, user_id):

    logger.info(f"Testing user ID: {user_id}")

    response = api_client.get(f"/users/{user_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == user_id

    logger.info(f"User ID {user_id} test passed")