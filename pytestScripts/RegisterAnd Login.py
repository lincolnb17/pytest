#importing modules
import requests
import json
def test_register_user():
    url="http://restapi.adequateshop.com/api/authaccount/registration"

    data = {
    'name':"Lincoln",
    'email':'bhattachanl1d7@gmail.com',
    'password':'123456'
    }
    register_data = json.dumps(data)
    headers = {"Content-Type": "application/json; charset=utf-8"}

    # sending post request
    res = requests.post(url,register_data, headers=headers)
    print(res.content)
    #validating status code
    json_res1 = json.loads(res.text)
    print(json_res1)
    assert res.status_code == 200

def test_login_user():
    url ="http://restapi.adequateshop.com/api/authaccount/login"
    data = {
    'email':'Developer51@gmail.com',
    'password':'123456'
    }
    login_data = json.dumps(data)
    headers = {"Content-Type": "application/json; charset=utf-8"}

    # sending post request
    res = requests.post(url,login_data, headers=headers)
    # print(res.content)
    #validating status code
    assert res.status_code == 200
    json_res = json.loads(res.text)
    print(json_res["code"])
    print(json_res)





