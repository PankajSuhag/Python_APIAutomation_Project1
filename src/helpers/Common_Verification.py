def verify_http_code(response, expected):
    assert response.status_code == int(expected)


def verify_key(response):
    assert response.json()["bookingid"] != 0, "Key is non empty : " + response
