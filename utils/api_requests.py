import requests

from config import DEFAULT_USERNAME, DEFAULT_PASSWORD, BASE_URL


class API:
    def __init__(self):
        self.token = None

    def user_login(self, username=DEFAULT_USERNAME, password=DEFAULT_PASSWORD):
        url = BASE_URL + ":8000/api/v1/accounts/staff_login/"
        payload = {
            "username": username,
            "password": password
        }

        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            self.token = data.get("token")
        else:
            raise Exception(f"Login failed username:{username} password:{password}")

    def get_search_response (self, endpoint: str):
        if self.token is None:
            self.user_login()
        headers = {
            "Authorization": f"Token {self.token}",
            "Content-Type": "application/json"
        }

        response = requests.get(endpoint, headers=headers)
        return response
