import requests
import json
import jsonpath

def test_add_new_data():
    #add student
    url = "http://thetestingworldapi.com/api/studentDetails"
    infile = open("C:\\Users\\petro\\Repos\\python\\APITesting\\test.json", "r")
    json_input = infile.read() #string format now
    request_json = json.loads(json_input)  #makes it into json format
    response = requests.post(url, request_json)
    id = jsonpath.jsonpath(response.json(), "id") #get its id
    print(id[0]) 

    #add tech details
    tech_api_url = "http://thetestingworldapi.com/api/technicalskills"
    infile = open("C:\\Users\\petro\\Repos\\python\\APITesting\\test.json", "r")
    json_input = infile.read() #string format now
    request_json = json.loads(json_input)  #makes it into json format
    #make ids consistent
    request_json['id'] = int(id[0])
    request_json['st_id'] = int(id[0])
    response = requests.post(tech_api_url, request_json)

    #add address
    ad_api_url = "http://thetestingworldapi.com/api/addresses"
    infile = open("C:\\Users\\petro\\Repos\\python\\APITesting\\test.json", "r")
    json_input = infile.read() #string format now
    request_json = json.loads(json_input)  #makes it into json format
    request_json['stId'] = int(id[0])
    response = requests.post(ad_api_url, request_json)

    #get the final details of the person
    final_details = "http://thetestingworldapi.com/api/FinalStudentDetails/" + int(id[0])
    requests.get(final_details)


