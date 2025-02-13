import allure
import requests
from faker import Faker
import random
import os
from dotenv import load_dotenv

load_dotenv()
fake = Faker()


HOST = "https://restful-booker.herokuapp.com"


class UpdateBooking:
    @allure.step("Updates a current booking")
    def update_booking(self, booking_id):
        """Обновляет текущее бронирование"""
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
            "Content-Type": "application/json",
            "Accept": "application/json",
            'Authorization': f"{os.getenv('authorization')}"
        }
        response = requests.put(f"{HOST}/booking/{booking_id}", headers=headers, json=payload)
        assert response.status_code == 200, response.status_code
        print(response.json())
        assert payload['firstname'] == response.json()['firstname']
        assert payload['lastname'] == response.json()['lastname']
        assert payload['totalprice'] == response.json()['totalprice']
        assert payload['depositpaid'] == response.json()['depositpaid']
        assert payload['bookingdates']['checkin'] == response.json()['bookingdates']['checkin']
        assert payload['bookingdates']['checkout'] == response.json()['bookingdates']['checkout']
        assert payload['additionalneeds'] == response.json()['additionalneeds']