def create_booking_data():
    payload = {
        "firstname": "Pankaj",
        "lastname": "Suhag",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "Breakfast, Lunch, Dinner",
    }

    return payload


def full_update_booking_data():
    payload = {
        "firstname": "Pankaj",
        "lastname": "Suhag full updated ",
        "totalprice": 115,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast,lunch,dinner"
    }
    return payload

def full_update_headers(token):
    temp_token = "token=" + str(token)
    header = {
        "Content-Type": "application/json",
        "cookie": temp_token
    }
    return header

def partial_update_booking_data():
    payload = {
        "firstname": "Pankaj",
        "lastname": "Panku patch updated",
    }

def partial_update_booking_header(token):
    temp_token="token="+str(token)
    header = {
        "Content-Type": "application/json",
        "cookie": temp_token,
        "Accept": "application/json"
    }
    return header

def create_booking_token_header():
    header = {
        "Content-Type": "application/json"
    }
    return header


def create_token_cred():
    payload = {

        "username": "admin",
        "password": "password123"
    }
    return payload
