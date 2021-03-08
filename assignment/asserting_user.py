import requests

url = "https://reqres.in/api/users/2"
resp = requests.get(url)
json_response = resp.json()

print("id :" , json_response["data"]["id"])
assert json_response["data"]["id"] == 2

print(json_response["data"]["first_name"])
print(json_response["data"]["first_name"]) == "John"