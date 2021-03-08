import requests

url = "https://reqres.in/api/users?page=2"
paramvalue = {"page":2}
resp = requests.get(url, params=paramvalue)
json_response = resp.json()
print("page no:" , json_response['page'])
assert json_response['page'] == 2

print("id :" , json_response["data"][0]["id"])
assert json_response["data"][0]["id"] == 7

print(json_response["data"][0]["last_name"])
print(json_response["data"][0]["last_name"]) != "lokesh"