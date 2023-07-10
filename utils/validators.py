class Validator():
    def validate_response_count(self, response):
        if response.status_code == 200:
            data = response.json()
            assert len(data["results"]) == 1
        else:
            raise Exception(f"Error: {response.status_code} - {response.text}")