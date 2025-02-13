import allure
import pytest
import requests
from faker import Faker
import random
import os
from dotenv import load_dotenv

fake = Faker()
load_dotenv()

HOST = "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="function")
def create_token():
    """Создает новый токен аутентификации"""
    payload = {
        "username": f"{os.getenv('user_name')}",
        "password": f"{os.getenv('password')}"
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(f"{HOST}/auth", headers=headers, json=payload)
    assert response.status_code == 200, response.status_code
    print(response.status_code)
    assert response.json()['token'] != 0 or response.json()['token'] != "", "Токен отсутствует!"
    print(response.json())
    token = response.json()['token']
    yield token


@pytest.fixture(scope="function", autouse=True)
def create_booking():
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
    yield booking_id