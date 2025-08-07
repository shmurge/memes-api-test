import os
from dotenv import load_dotenv
import allure
import requests
from api_client.base_api import BaseApi
from api_client.memes_api.memes_endpoints import MemesEndpoints
from assertions.memes_assertions import MemesAssertions
from api_client.memes_api.models.response_memes_models import ResponseMemeModel, ResponseMemeListModel

load_dotenv()


class MemesApi(BaseApi):

    def __init__(self):
        super().__init__()

        self.endpoints = MemesEndpoints()
        self.username = os.getenv('USERNAME')
        self.assertions = MemesAssertions()

    def create_meme(self, payload):
        with allure.step("Создать мем"):
            resp = requests.post(
                url=self.endpoints.create_meme,
                headers=self.headers.headers_with_auth(),
                json=payload.model_dump()
            )

            self.assertions.check_status_code_is_200(resp)
            self.assertions.check_meme_fields(payload, ResponseMemeModel(**resp.json()))
            self.attach_response(resp.json())

            return ResponseMemeModel(**resp.json())

    def update_meme(self, mem_id, payload):
        with allure.step(f"Изменить мем с id: {mem_id}"):
            resp = requests.put(
                url=self.endpoints.update_meme(mem_id),
                headers=self.headers.headers_with_auth(),
                json=payload.model_dump()
            )

            self.assertions.check_status_code_is_200(resp)
            self.attach_response(resp.json())

            return ResponseMemeModel(**resp.json())

    def get_meme_by_id(self, mem_id):
        with allure.step(f"Вернуть мем с id: {mem_id}"):
            resp = requests.get(
                url=f"{self.endpoints.get_all_memes}/{mem_id}",
                headers=self.headers.headers_with_auth()
            )

            self.assertions.check_status_code_is_200(resp)
            self.assertions.id_should_not_change(mem_id, ResponseMemeModel(**resp.json()).id)
            self.attach_response(resp.json())

            return ResponseMemeModel(**resp.json())

    def get_all_memes(self):
        with allure.step("Вернуть все мемы"):
            resp = requests.get(
                url=self.endpoints.get_all_memes,
                headers=self.headers.headers_with_auth()
            )

            self.assertions.check_status_code_is_200(resp)
            self.attach_response(resp.json())

            return ResponseMemeListModel(**resp.json())

    def delete_meme(self, mem_id):
        with allure.step(f"Удалить мем с id: {mem_id}"):
            resp = requests.delete(
                url=self.endpoints.delete_meme(mem_id),
                headers=self.headers.headers_with_auth()
            )

            self.assertions.check_status_code_is_200(resp)
            self.assertions.check_message_after_meme_deleting(mem_id, resp.text)
            self.attach_response(resp.text)
