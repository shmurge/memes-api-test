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
        with allure.step('User authorization'):

            resp = requests.post(
                url=self.base_endpoints.authorization,
                headers=self.headers.base_headers,
                json=payload.model_dump()
            )

            self.base_assertions.check_status_code_is_200(resp)
            self.attach_response(resp.json())

            return ResponseAuthorizationModel(**resp.json())


    def api_token_is_alive(self, token):
        with allure.step('Checking api token is alive'):

            try:
                resp = requests.get(
                    url=self.base_endpoints.is_token_alive(token)
                )

                self.base_assertions.check_status_code_is_200(resp)
            except:
                return False

            return True
