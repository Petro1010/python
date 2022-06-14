import json
from urllib import response
import requests

url = "https://reqres.in/api/users?page=2"
response = requests.get(url)

#get response code
response_code = response.status_code

assert response_code == 200, "Code does not match"

#get the data in json version
json_data = response.json()

#print(response.text)  string version of data
#print(response.content)  byte version of data
#print(response.headers)
#print(response.cookies)
#print(response.encoding)
#print(response.url)
#print(response.json())  # json version of response

assert json_data["total_pages"] == 2, "Total page count not matching"
assert json_data["total"] == 12

print(json_data["data"][0]["email"]) #getting a specific index of data

assert json_data["data"][0]["email"].endswith("reqres.in"), "Email format is not matching"

assert json_data["data"][0]["first_name"] == "Michael"