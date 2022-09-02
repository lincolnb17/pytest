#importing modules
import pytest
import requests

#API_URL
url = "https://reqres.in/api/users/2"
#sending get request
res = requests.get(url)
print(res.content)
if res.status_code==200:
    print("Test Passed")
else:
    print("Test Failed")

