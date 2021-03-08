import requests
import json

payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

resp = requests.post("https://reqres.in/api/register", data=payload)
print(resp.status_code)
print(json.dumps(resp.json(), indent = 4))

#Testing for logging with the registered user
res = requests.post("https://reqres.in/api/login",  data=payload)
print(res.status_code)
print(json.dumps(res.json(), indent=4))