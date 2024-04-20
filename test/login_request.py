import requests
import json

data = json.dumps({
    'username': '1111',
    'password': '2222',
})

response = requests.post(url='http://127.0.0.1:5000/login', data=data)
print(response.text)