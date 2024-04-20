import requests
import json

data = json.dumps({
    'username': '9',
    'password': '9',
})

response = requests.post(url='http://127.0.0.1:5000/register', data=data)
print(response.text)