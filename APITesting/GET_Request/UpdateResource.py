import requests
import json
import jsonpath

# Put (update) request url
url = "https://reqres.in/api/users/2" #include the id to update at the end

# First make a json file with the input content

# Now read the input Json file
infile = open("C:\\Users\\petro\\Repos\\python\\APITesting\\test.json", "r")  #read the data
json_input = infile.read() #string format now
request_json = json.loads(json_input)  #makes it into json format

# Make the put request with json Input body and get the response
response = requests.put(url, request_json)

# validate the response code
assert response.status_code == 200

# Parse Content
reponse_json = response.json()
print(reponse_json)

updated = reponse_json["first_name"]
print(updated)