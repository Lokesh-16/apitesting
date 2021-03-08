import requests


resp = requests.get("https://reqres.in/api/unknown")
json_response = resp.json()
print("page no:" , json_response['page'])
assert json_response['page'] == 1

print("id :" , json_response["data"][1]["id"])
assert json_response["data"][1]["id"] == 2

print(json_response["data"][1]["year"])
print(json_response["data"][1]["year"]) !=2002