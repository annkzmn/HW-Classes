import requests
import pprint

print('Hello')

def test_first():
    url = "https://send-request.me/api/users"
    data = {
        "first_name": "Giorgiana",
        "last_name": "Diki",
         "company_id": 1
    }

    response = requests.post(url, json=data)
    print(response.json())