"""Validating user creation,update and delete"""
import requests
from utilities.configurations import *
from utilities.resources_api import *
from utilities.payLoad import *

user_payload = get_user_payload()
auth_token = None
user_id = None
url = get_config()['API']['end_url']


# validate if user details are matching from the output obtained

def assert_user_response(user_payload, res):
    assert res['userId'] != ''
    assert res['name'] == user_payload['name'], 'Mismatch in the name'
    assert res['email'] == user_payload['email'], 'Mismatch in the email'
    assert res['roles'][0] == 'USER', 'Mismatch in the User role'


# creating a user with all details sent in payload and obtain token and userID
def create_user_test():
    global auth_token
    global user_id
    response = requests.post(url + api_resources.create_user,
                             json=user_payload, headers=get_headers())
    res = response.json()
    print("users details= ", res)
    assert response.status_code == 201
    auth_token = res["token"]
    user_id = res["userId"]
    assert_user_response(user_payload, res)
    print("user created successfully")


# Once user created retrieve the data and validate it
def get_user_test():
    res_url = url + api_resources.get_user + user_id
    print("resoruce url= " + res_url)
    response = requests.get(res_url, headers=get_headers(token=auth_token))
    assert response.status_code == 200, "Unexpected status code"
    assert_user_response(user_payload, response.json())
    print("user retrieved successfully")


# update the user by username and validate it
def update_user_test():
    put_url = url + api_resources.get_user + user_id
    payload = put_user_payload()
    response = requests.put(put_url, json=payload,
                            headers=get_headers(token=auth_token))

    assert response.status_code == 200, "expected 200 code but found" + str(response.status_code)
    # response = requests.get(put_url, headers=get_headers(token=auth_token))
    res = response.json()
    for attrb in payload["attributesToBeUpdated"]:
        assert res[attrb] == payload[attrb], "Expected " + attrb + " is " + payload[attrb] + " but found " + str(
            res[attrb])
        print("username updated successfully")


# delete the user which is created
def delete_user_test():
    del_url = url + api_resources.get_user + user_id
    response = requests.delete(del_url, headers=get_headers(token=auth_token))
    assert response.status_code == 200, "expected status code is 200 but found" + str(response.status_code)
    print("user deleted successfully")


# methods to perform all API operations
create_user_test()
get_user_test()
update_user_test()
delete_user_test()
