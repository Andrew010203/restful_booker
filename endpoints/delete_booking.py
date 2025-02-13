import allure
import requests
import os
from dotenv import load_dotenv

load_dotenv()



HOST = "https://restful-booker.herokuapp.com"


class DeleteBooking:
    @allure.step("Delete booking")
    def delete_booking(self, booking_id):
        """Удаляет идентификатор бронирования"""
        payload = {
        }
        headers = {
            "Content-Type": "application/json",
            'Authorization': f"{os.getenv('authorization')}"
        }
        response = requests.delete(f"{HOST}/booking/{booking_id}", headers=headers, json=payload)
        assert response.status_code == 201, response.status_code
        print(response.status_code)
        # Проверка, что созданный ранее id бронирования был удален
        response = requests.get(f"{HOST}/booking/{booking_id}", headers=headers, json=payload)
        assert response.status_code == 404, response.status_code
        print(response.status_code)

