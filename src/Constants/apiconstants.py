# Add your url constants

# Adding my url constants

def base_url():
    return "https://restful-booker.herokuapp.com"


def url_get_all_bookings():
    return "https://restful-booker.herokuapp.com/booking"


def url_get_specific_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)


def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"


def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"


def url_update_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + booking_id
