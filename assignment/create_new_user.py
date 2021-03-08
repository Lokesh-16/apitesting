import requests
import json

payload = {
    "name": "lokesh",
    "job": "testere"
}
resp = requests.post("https://reqres.in/api/users", data=payload)
print (resp)
print(json.dumps(resp.json(), indent = 4))

list_users = requests.get("https://reqres.in/api/users?page=155")
print(json.dumps(list_users.json(), indent = 4))
