import allure
import requests

HOST = "https://restful-booker.herokuapp.com"

class GetBookingids:
    @allure.step("Returns the ids of all the bookings")
    def get_bookingids(self):
        """Возвращает идентификаторы всех бронирований"""
        payload = {}
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.get(f"{HOST}/booking", headers=headers, json=payload)
        assert response.status_code == 200, response.json()
        print(response.json())