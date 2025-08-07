import allure
import requests
from assertions.base_assertions import BaseAssertions
from api_client.base_endpoints import BaseEndpoints
from api_client.base_models import ResponseAuthorizationModel
from config.headers import Headers
from utils.helper import Helper


class BaseApi(Helper):

    def __init__(self):
        super().__init__()
        self.base_endpoints = BaseEndpoints()
        self.headers = Headers()
        self.base_assertions = BaseAssertions()

    def user_authorization(self, payload):
        with allure.step('Авторизация'):
            resp = requests.post(
                url=self.base_endpoints.authorization,
                headers=self.headers.base_headers,
                json=payload.model_dump()
            )

            self.base_assertions.check_status_code_is_200(resp)
            self.attach_response(resp.json())

            return ResponseAuthorizationModel(**resp.json())

    def api_token_is_alive(self, token):
        with allure.step('Проверка состояния токена'):
            resp = requests.get(
                url=self.base_endpoints.is_token_alive(token)
            )

            return True if resp.status_code == 200 else False

    def auth_with_invalid_data(self, payload):
        with allure.step('Авторизация с невалидными кредами'):
            resp = requests.post(
                url=self.base_endpoints.authorization,
                headers=self.headers.base_headers,
                json=payload.model_dump()
            )

            self.base_assertions.check_status_code_is_400(resp)
