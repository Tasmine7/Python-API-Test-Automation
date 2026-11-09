import pytest
from api_client import APIClient


@pytest.fixture
def api_client():
    base_url = "https://jsonplaceholder.typicode.com"
    return APIClient(base_url)