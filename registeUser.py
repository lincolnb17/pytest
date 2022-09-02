#importing modules
from email import header
import pytest
import requests
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
user1 = User('Lincoln', 'lincoln123@nepal.com','Hello123')

#convert to JSON string
loginDetails = json.dumps(user1.__dict__)

headers = {"Content-Type": "application/json; charset=utf-8"}
#sending post request
res = requests.post(url,loginDetails,headers=headers)
print(res.content)
if res.status_code==200:
    print("Test Passed")
else:
    print("Test Failed")

