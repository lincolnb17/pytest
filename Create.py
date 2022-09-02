#importing modules
import requests
import json
#API_URL FOR CREATE USER
#METHOD=POST
url ="https://reqres.in/api/users"

#reading  login data from json file
loginData= open('D:\\freelance\\pytest\\data\\loginData.json', 'r')
json_input = loginData.read()
request_json = json.loads(json_input)

#sending post request with json body
res = requests.post(url,json_input)
print(res.content)
if res.status_code==201:
    print("Test Passed")
else:
    print("Test Failed")




