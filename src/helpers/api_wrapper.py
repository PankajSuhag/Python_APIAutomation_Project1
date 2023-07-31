import requests
from src.helpers.Common_Verification import *


def post_request(url, headers, payload):
    post_response_data = requests.post(url=url, headers=headers, json=payload)
    status_code = verify_http_code(post_response_data, "200")

    verify_key(post_response_data)
    return post_response_data.json()


def put_request(url, headers, payload):
    put_response_data = requests.put(url=url, headers=headers, json=payload)
    status_code = verify_http_code(put_response_data, "200")
    return put_response_data.json()

def patch_request(url, headers, payload):
    put_response_data = requests.put(url=url, headers=headers, json=payload)
    status_code = verify_http_code(put_response_data, "200")
    return put_response_data.json()

def get_all_request(url):
    get_request_data = requests.get(url=url)
    status_code = verify_http_code(get_request_data, "200")

    return get_request_data.json()


def get_specific_requestid(url):
    get_request_data = requests.get(url=url)
    status_code = verify_http_code(get_request_data, "200")

    # return get_specific_requestid.json()


def create_token(url, headers, payload):
    response = requests.post(url=url, headers=headers, json=payload)
    verify_http_code(response, 200)
    assert len(response.text) > 0
    assert response.text.__contains__("token")
    print(response.json()["token"])
    return response.json()["token"]
