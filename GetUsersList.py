#importing modules
import pytest
import requests

#API_URL
#METHOD=GET
url = "https://reqres.in/api/users?page=2"
#sending get request
res = requests.get(url)
print(res.content)

#validating status code  and  this can also check by assert function
if res.status_code==200:
    print("Test Passed")
else:
    print("Test Failed")

