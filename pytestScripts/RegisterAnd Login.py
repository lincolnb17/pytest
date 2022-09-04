#importing modules
import requests
import json
import  pytest

def test_register_user():
    url="http://restapi.adequateshop.com/api/authaccount/registration"

    data = {
    'name':"Lincoln",
    'email':'laddffffdasdsd1ddd1sddddd123o1@gmail.com',
    'password':'123456'
    }
    register_data = json.dumps(data)
    headers = {"Content-Type": "application/json; charset=utf-8"}


    # sending post request
    res = requests.post(url,register_data, headers=headers)
    # print(res.content)
    #validating status code
    print(type(res))
    json_res1 = json.loads(res.content)
    print(json_res1)
    token=(json_res1["data"]["Token"])
    assert res.status_code == 200
    print (token)
def test_login_user():
    url ="http://restapi.adequateshop.com/api/authaccount/login"
    data = {
    'email':'Developer5@gmail.com',
    'password':'123456'
    }
    login_data = json.dumps(data)
    headers = {"Content-Type": "application/json; charset=utf-8"}

    # sending post request
    res = requests.post(url,login_data, headers=headers)
    # print(res.content)
    #validating status code

    json_res = json.loads(res.content)
    # print(json_res["code"])
    # print(json_res)
    assert res.status_code == 200


def test_update_info():
    url= "https://reqres.in/api/users/2"
    data = {
    'name': "morpheus",
    'job': "zion resident"
    }
    update_data = json.dumps(data)
    res = requests.put(url,update_data)
    print(res.content)

    #validationn status code
    assert res.status_code == 200

