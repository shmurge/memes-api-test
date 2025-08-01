import allure
import requests
from api_client.base_api import BaseApi
from api_client.memes.memes_endpoints import MemesEndpoints
from api_client.memes.payloads import MemesPayloads
from api_client.memes.models.response_memes_models import ResponseMemeModel


class MemesApi(BaseApi):

    def __init__(self):
        super().__init__()

        self.endpoints = MemesEndpoints()
        self.payloads = MemesPayloads()

    def create_meme(self, payload=None):
        with allure.step("Create meme"):
            payload = payload if payload else self.payloads.create_meme
            resp = requests.post(
                url=self.endpoints.create_meme,
                headers=self.headers.headers_with_auth,
                json=payload.model_dump()
            )

            self.base_assertions.check_status_code_is_200(resp)
            self.attach_response(resp.json())

            return ResponseMemeModel(**resp.json())
