import allure
import requests
from faker import Faker
import random

fake = Faker()

HOST = "https://restful-booker.herokuapp.com"


class CreateBooking:
    @allure.step("Creates a new booking in the API")
    def create_booking(self):
        """Создает новое бронирование в API"""
        payload = {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "totalprice": random.randint(1, 200),
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(f"{HOST}/booking", headers=headers, json=payload)
        assert response.status_code == 200, response.json()
        print(response.json())
        booking_id = response.json()['bookingid']
        assert payload['firstname'] == response.json()['booking']['firstname']
        assert payload['lastname'] == response.json()['booking']['lastname']
        assert payload['totalprice'] == response.json()['booking']['totalprice']
        assert payload['depositpaid'] == response.json()['booking']['depositpaid']
        assert payload['bookingdates']['checkin'] == response.json()['booking']['bookingdates']['checkin']
        assert payload['bookingdates']['checkout'] == response.json()['booking']['bookingdates']['checkout']
        assert payload['additionalneeds'] == response.json()['booking']['additionalneeds']
        print(booking_id)
        return booking_id