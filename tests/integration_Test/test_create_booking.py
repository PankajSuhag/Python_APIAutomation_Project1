'''
Author: Pankaj
Objective: Create and Verify by POST Request
TC#1 - Verify the Status Code, Headers
TC#2 - Verify the Body -> Booking_id
TC#3 - Verify the JSON Schema is Valid
'''

import pytest
import requests
from src.helpers.Payload_manager import create_booking_data, create_booking_token_header, create_token_cred, \
    full_update_booking_data,full_update_headers, partial_update_booking_data, partial_update_booking_header
from src.Constants.apiconstants import url_create_booking, url_get_all_bookings, url_get_specific_booking, \
    url_create_token, url_update_delete_booking
from src.helpers.api_wrapper import post_request, get_all_request, get_specific_requestid, create_token, put_request


class Testintegration(object):

    @pytest.fixture
    def test_create_token_req(self):
        payload = create_token_cred()
        headers = create_booking_token_header()
        response = create_token(url_create_token(), headers, payload)
        return response

    @pytest.fixture
    def test_create_booking_tc1(self):
        payload = create_booking_data()
        url = url_create_booking()
        headers = create_booking_token_header()
        response = post_request(url, headers, payload)
        print(response)
        print(response["bookingid"])
        booking_id = response["bookingid"]
        return booking_id

    def test_get_all_bookingid_req(self):
        response = get_all_request(url_get_all_bookings())
        print(response)

    def test_specific_bookingid_req(self, test_create_booking_tc1):
        response = get_specific_requestid(url_get_specific_booking(test_create_booking_tc1))
        print(response)

    def test_put_request(self, test_create_token_req, test_create_booking_tc1):

        payload = full_update_booking_data()
        header=full_update_headers(test_create_token_req)
        url = url_update_delete_booking(str(test_create_booking_tc1))

        response = put_request(url, header, payload)
        response = requests.put(url, headers=header, json=payload)

        print(response.json())
        print(response.text)
        print("In put request=", test_create_booking_tc1, test_create_token_req)


    def test_patch_request(self, test_create_token_req, test_create_booking_tc1):

         payload= partial_update_booking_data()
         header=partial_update_booking_header(test_create_token_req)

         url = url_update_delete_booking(str(test_create_booking_tc1))
         response = requests.patch(url, headers=header, json=payload)

         print(response.json())
         print(response.text)
         print("In patch request=", test_create_booking_tc1, test_create_token_req)

