from logger_config import logger


def test_delete_user(api_client):

    logger.info("Starting DELETE test")

    response = api_client.delete("/users/1")

    assert response.status_code == 200

    logger.info("DELETE test passed")