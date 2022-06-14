import requests
import json
import jsonpath

# our API url:
url = "https://reqres.in/api/users?page=2"

# Send Get Request to API, retrieve response from server
response = requests.get(url)

# display response content
#print(response.content)
#print(response.headers)

# parse response to json format
json_response = json.loads(response.text)
#print(json_response)

# fetch a value from response using Json Path
pages = json_response['total_pages']
print(pages)
#validate the value we fetched
assert pages == 2
