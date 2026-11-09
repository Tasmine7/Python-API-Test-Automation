import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint):
        return self.session.get(
            f"{self.base_url}{endpoint}",
            timeout=10
        )

    def post(self, endpoint, payload):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            json=payload,
            timeout=10
        )

    def put(self, endpoint, payload):
        return self.session.put(
            f"{self.base_url}{endpoint}",
            json=payload,
            timeout=10
        )

    def delete(self, endpoint):
        return self.session.delete(
            f"{self.base_url}{endpoint}",
            timeout=10
        )