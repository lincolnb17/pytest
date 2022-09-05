#importing modules
import requests
import json
import  pytest

def test_register_user():
    url="http://restapi.adequateshop.com/api/authaccount/registration"
    data = {
    'name':"Lincoln",
    'email':'tristin3D2a@gmail.com',
    'password':'123456'
    }
    register_data = json.dumps(data)
    headers = {"Content-Type": "application/json; charset=utf-8"}

    # sending post request
    res = requests.post(url,register_data, headers=headers)
    # print(res.content)
    #validating status code
    json_res1 = json.loads(res.content)
    print(res.content)
    email=(json_res1["data"]["Email"])
    ## login request
    url2 ="http://restapi.adequateshop.com/api/authaccount/login"
    data2 = {
        'email': email,
        'password': '123456'
    }
    login_data = json.dumps(data2)
    #sending post api call for login
    res2 = requests.post(url2,login_data,headers=headers)
    print(res2.content)
    #validating status code
    assert res.status_code and res2.status_code == 200
