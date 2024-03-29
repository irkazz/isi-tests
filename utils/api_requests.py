import json
import os

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

    def create_payer_api(self, timestamp):
        if self.token is None:
            self.user_login()

        endpoint = BASE_URL + ':8000/api/v1/accounts/account/'

        # Get the current working directory
        current_directory = os.getcwd()

        # Join the current directory with the filename to get the absolute path
        file_path = os.path.join(current_directory, 'test_data/payer.json')

        # Read the payload from the JSON file
        with open(file_path) as file:
            payload = json.load(file)

        # Update the name and account_id with timestamp
        payload['name'] += timestamp
        payload['account_id'] += timestamp

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

    def create_passenger_api(self, timestamp):
        if self.token is None:
            self.user_login()

        endpoint = BASE_URL + ':8000/api/v1/accounts/client/'

        # Get the current working directory
        current_directory = os.getcwd()

        # Join the current directory with the filename to get the absolute path
        file_path = os.path.join(current_directory, 'test_data/passenger.json')

        # Read the payload from the JSON file
        with open(file_path) as file:
            payload = json.load(file)

        # Update the name and account_id with timestamp
        payload['first_name'] += timestamp
        payload['last_name'] += timestamp

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

    def deactivate_object_api(self, endpoint):
        if self.token is None:
            self.user_login()

        # Set the request headers
        headers = {
            "Authorization": f"Token {self.token}",
            "Content-Type": "application/json"
        }

        # Make the DELETE request
        response = requests.delete(endpoint, headers=headers)
        return response

    def deactivate_payer_api(self, payer_id):
        endpoint = BASE_URL + f":8000/api/v1/accounts/account/{payer_id}/?show_inactive=yes"
        return self.deactivate_object_api(endpoint)

    def deactivate_passenger_api(self, passenger_id):
        endpoint = BASE_URL + f":8000/api/v1/accounts/client/{passenger_id}/?show_inactive=yes"
        return self.deactivate_object_api(endpoint)