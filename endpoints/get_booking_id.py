import allure
import requests
import random

HOST = "https://restful-booker.herokuapp.com"
random_id = random.randint(1, 100)

class GetBookingId:
    @allure.step("Returns a specific booking based upon the booking id provided")
    def get_booking_id(self):
        """Возвращает конкретное бронирование на основе id"""
        payload = {}
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.get(f"{HOST}/booking/{random_id}", headers=headers, json=payload)
        assert response.status_code == 200, response.json()
        print(response.json())
        response_data = response.json()
        assert 'firstname' in response_data
        assert 'lastname' in response_data
        assert 'totalprice' in response_data
        assert 'depositpaid' in response_data
        assert 'checkin' in response_data['bookingdates']
        assert 'checkout' in response_data['bookingdates']
