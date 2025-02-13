import allure
import requests
from faker import Faker
import random
import os
from dotenv import load_dotenv

load_dotenv()
fake = Faker()

HOST = "https://restful-booker.herokuapp.com"


class PartialUpdateBooking:
    @allure.step("Updates a current booking with a partial payload")
    def partial_update_booking(self, booking_id):
        """Обновляет текущее бронирование с частичной полезной нагрузкой"""
        payload = {
            "firstname": fake.first_name(),
            "lastname": fake.last_name()
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            'Authorization': f"{os.getenv('authorization')}"
        }
        response = requests.patch(f"{HOST}/booking/{booking_id}", headers=headers, json=payload)
        assert response.status_code == 200, response.status_code
        print(response.json())
        assert payload['firstname'] == response.json()['firstname']
        assert payload['lastname'] == response.json()['lastname']
