import json
import time

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

    def get_search_response(self, endpoint: str):
        if self.token is None:
            self.user_login()
        headers = {
            "Authorization": f"Token {self.token}",
            "Content-Type": "application/json"
        }

        response = requests.get(endpoint, headers=headers)
        return response

    def create_payer_api(self):
        if self.token is None:
            self.user_login()

        endpoint = BASE_URL + ':8000/api/v1/accounts/account/'

        # Generate timestamp
        timestamp = str(int(time.time()))

        # Read the payload from the JSON file
        with open('payer.json') as file:
            payload = json.load(file)

        # Update the name and account_id with timestamp
        payload['name'] += "_" + timestamp
        payload['account_id'] += "_" + timestamp

        # Convert the payload to JSON
        json_payload = json.dumps(payload)

        # Set the request headers
        headers = {
            "Authorization": f"Token {self.token}",
            "Content-Type": "application/json"
        }

        # Make the POST request
        response = requests.post(endpoint, data=json_payload, headers=headers)
        return response