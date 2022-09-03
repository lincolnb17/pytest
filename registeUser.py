#importing modules
from email import header, message
import requests
import jsonpath
import json

#API_URL FOR CREATE USER
#METHOD=POST
url = "http://restapi.adequateshop.com/api/authaccount/registration"

#creating class
class User:
	def __init__(self, name,email, password):
		self.name = name
		self.email = email
		self.password = password
#create object
user1 = User('Lincoln', 'lincoln12ds43@nepal.com','Hello123')

#convert to JSON string
loginDetails = json.dumps(user1.__dict__)

headers = {"Content-Type": "application/json; charset=utf-8"}
#sending post request
res = requests.post(url,loginDetails,headers=headers)
print(res.content)
#fetching data from json response
json_res = json.loads(res.text)
message=jsonpath.jsonpath(json_res,'message')
## validating response message
if message[0]=='success':
    print("Test Passed")
else:
    print("Test Failed")

