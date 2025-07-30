import json
import requests
from requests.auth import HTTPBasicAuth

# Use to make a POST request to a specific endpoint and return the result body json
# Example: get demographics with url='https://uat-routeapi.mediatel.co.uk/rest/demographics'


def get_data(url, username, password, apikey, request):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Api-Key": apikey,
    }

    auth = HTTPBasicAuth(username, password)
    try:
        response = requests.post(
            url, headers=headers, data=json.dumps(request), auth=auth
        )
        response.raise_for_status()
        print("Success:", response.json())
    except requests.exceptions.RequestException as e:
        print("Error:", e, response.headers, response.content)

    return response.json()
