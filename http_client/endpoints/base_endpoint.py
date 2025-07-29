import allure
import requests
from http_client.endpoints.headers import base_headers, headers_with_auth
from http_client.assertions.base_assertions import BaseAssertions
from http_client.models.base_models import ResponseAuthorizationModel


class BaseEndpoint:

    def __init__(self):
        self.base_url = 'http://memesapi.course.qa-practice.com'
        self.headers = headers_with_auth
        self.base_assertions = BaseAssertions()


    def user_authorization(self, payload, headers=base_headers):
        with allure.step('User authorization'):
            path = f'{self.base_url}/authorize'
            headers = headers if headers else self.headers

            resp = requests.post(
                url=path,
                headers=headers,
                json=payload.model_dump()
            )

            BaseAssertions().check_status_code_is_200(resp)

            return ResponseAuthorizationModel(**resp.json())


    def api_token_is_alive(self, token):
        with allure.step('Checking api token is alive'):
            path = f'{self.base_url}/authorize/{token}'
            try:
                resp = requests.get(
                    url=path
                )

                BaseAssertions().check_status_code_is_200(resp)
            except:
                return False

            return True



