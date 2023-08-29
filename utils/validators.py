class Validator:
    def validate_response_count(self, response):
        if response.status_code == 200:
            data = response.json()
            assert len(data["results"]) == 1
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")

    def validate_acc_created(self, response, timestamp):
        if response.status_code == 201:
            data = response.json()
            assert data['name'] == f"PY{timestamp}"
            assert data['account_id'] == f"PY{timestamp}"
            return data
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")

    def validate_client_created(self, response, timestamp):
        if response.status_code == 201:
            data = response.json()
            assert data['last_name'] == f"PASL{timestamp}"
            return data
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")

    def validate_object_deactivated(self, response):
        assert response.status_code == 204
