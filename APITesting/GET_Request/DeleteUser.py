import requests
import json
import jsonpath

# url for the user with id 2:
url = "https://reqres.in/api/users/2"

# Send delete Request to API, retrieve response from server
response = requests.delete(url)

print(response.status_code) #if sucessful we will get 204 back

#to check delete worked we check the status code
assert response.status_code == 204

#We can then run a get request and check that the specific user is deleted