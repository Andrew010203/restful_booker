import allure
import requests
import os
from dotenv import load_dotenv

load_dotenv()


HOST = "https://restful-booker.herokuapp.com"


class CreateToken:
    @allure.step("Creates a new auth token")
    def create_token(self):
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
        assert response.json()['token'] != 0 or response.json()['token'] != None, "Токен отсутствует!"
        print(response.json())
        token = response.json()['token']
        return token
