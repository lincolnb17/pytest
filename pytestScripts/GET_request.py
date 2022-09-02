#importing modules
import requests
def test_get_user_list():
    response = requests.get("https://reqres.in/api/users?page=2")

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200


