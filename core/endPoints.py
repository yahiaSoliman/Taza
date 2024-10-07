import requests
import json

from core.data_sets import DataSets


class EndPoints:

    @staticmethod
    def register(phone_number, password):
        random_name = DataSets.generate_random_name()

        payload_register = json.dumps({
            "phone": phone_number,
            "first_name": random_name,
            "last_name": random_name,
            "location": "Baghdad",
            "new_password": password
        })

        headers = {
            'Content-Type': 'application/json',
            'x-app-id': 'web'
        }

        url_register = "https://fastapi.staging.taza.creativeadvtech.ml/api/v1/auth/register"

        response = requests.request("POST", url_register, headers=headers, data=payload_register)
        return response

    @staticmethod
    def register_otp(phone_number):

        payload_otp = json.dumps({
            "phone": phone_number,
            "code": "1111"
        })

        headers = {
            'Content-Type': 'application/json',
            'x-app-id': 'web'
        }

        url_otp = "https://fastapi.staging.taza.creativeadvtech.ml/api/v1/auth/register/check"

        response = requests.request("POST", url_otp, headers=headers, data=payload_otp)
        return response

    @staticmethod
    def login(phone_number, password):
        url_login = "https://fastapi.staging.taza.creativeadvtech.ml/api/v1/auth/login"
        payload_login = json.dumps({
            "phone": phone_number,
            "password": password,
            "uuid": "ubuntu_3rd",
            "os": "Ubuntu 21",
            "device_name": "AOC"
        })
        headers_login = {
            'Content-Type': 'application/json',
            'x-app-id': 'web'
        }
        response = requests.request("POST", url_login, headers=headers_login, data=payload_login)
        return response

    @staticmethod
    def toggle_favorite_item(access_token):
        url = "https://fastapi.staging.taza.creativeadvtech.ml/api/v1/item/favourites/CN-CB-ROS-0000003"
        payload = {}
        token = 'Bearer ' + access_token
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'x-app-id': 'web',
            'Accept-Language': 'EN'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        return response

    @staticmethod
    def add_address(access_token):
        url = "https://fastapi.staging.taza.creativeadvtech.ml/api/v1/user/address"
        token = 'Bearer ' + access_token
        payload = json.dumps({
            "address_title": "Home",
            "nickname": "Home",
            "address_line1": "street name",
            "city": "city",
            "floor": "4",
            "flat": "2",
            "nearest_landmark": "some place",
            "latitude": "33.310596534650596",
            "longitude": "44.36798371374607",
            "building": "building name",
            "neighbourhood": "some place",
            "district": "some district"
        })
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'x-app-id': 'web',
            'Accept-Language': 'EN'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    @staticmethod
    def clear_cart(access_token):
        url = "https://fastapi.staging.taza.creativeadvtech.ml/api/v1/item/cart/update"
        token = 'Bearer ' + access_token
        payload = json.dumps([
            {
                "item_code": "",
                "qty": 0
            }
        ])
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'x-app-id': 'web',
            'Accept-Language': 'EN'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    @staticmethod
    def update_cart(access_token, cart_object):
        url = "https://fastapi.staging.taza.creativeadvtech.ml/api/v1/item/cart/update"
        token = 'Bearer ' + access_token
        payload = json.dumps(cart_object)
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'x-app-id': 'web',
            'Accept-Language': 'EN'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response

    @staticmethod
    def cancel_order(access_token, order_id):
        url = "https://fastapi.staging.taza.creativeadvtech.ml/api/v1/sales-order/cancel-order/" + order_id
        token = 'Bearer ' + access_token
        payload = json.dumps({
            "cancel_reason": "test reason of cancellation"
        })
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'x-app-id': 'web',
            'Accept-Language': 'EN'
        }
        response = requests.request("PUT", url, headers=headers, data=payload)
        return response

    @staticmethod
    def before_checkout(access_token):
        url = "https://fastapi.staging.taza.creativeadvtech.ml/api/v1/customer/before-checkout"

        token = 'Bearer ' + access_token

        payload = json.dumps({
            "items": [
                {
                    "item_code": "CN-CB-ROS-0000003",
                    "qty": 1
                }
            ],
            "address_name": "fhgfv-Personal"
        })
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'x-app-id': 'web',
            'Accept-Language': 'EN'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response

    @staticmethod
    def create_order(access_token, date):
        url = "https://fastapi.staging.taza.creativeadvtech.ml/api/v1/frappe/Sales Order"

        token = 'Bearer ' + access_token
        payload = json.dumps({
            "delivery_date": date,
            "shipping_address_name": "fhgfv-Personal",
            "items": [
                {
                    "item_code": "CN-CB-ROS-0000003",
                    "qty": 1
                }
            ]
        })
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json',
            'x-app-id': 'web',
            'Accept-Language': 'EN'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        return response
