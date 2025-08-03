import allure
import os
import requests
from dotenv import load_dotenv

from api_client.memes_api.memes_endpoints import MemesEndpoints
from assertions.base_assertions import BaseAssertions
from config.headers import Headers

load_dotenv()


class MemesAssertions(BaseAssertions):

    def __init__(self):
        super().__init__()

        self.username = os.getenv('USERNAME')
        self.endpoints = MemesEndpoints()
        self.headers = Headers()

    def check_meme_fields(self, payload, response):
        with allure.step('Check information of meme'):
            self.check_data_is_equal(payload.text, response.text)
            self.check_data_is_equal(payload.url, response.url)
            self.check_data_is_equal(payload.tags, response.tags)
            self.check_data_is_equal(payload.info, response.info)
            self.check_data_is_equal(self.username, response.updated_by)

    def id_should_not_change(self, exp_id, act_id):
        with allure.step('Meme id should not change'):
            self.check_data_is_equal(exp_id, act_id)

    def meme_should_not_be_found(self, mem_id):
        with allure.step(f"Meme with id {mem_id} should not be found"):
            resp = requests.get(
                url=f"{self.endpoints.get_all_memes}/{mem_id}",
                headers=self.headers.headers_with_auth
            )

            self.check_status_code_is_404(resp)

    def meme_should_be_in_list(self, memes_list, response):
        with allure.step('Meme should be in memes list'):
            assert self.is_data_in_array(response, memes_list), (f'Meme not found in memes list!\n'
                                                                 f'{response}')

            for meme in memes_list:
                if meme.id == response.id:
                    self.check_meme_fields(meme, response)
                    break

    def meme_should_not_be_in_list(self, memes_list, response):
        with allure.step('Meme should not be in memes list'):
            assert not self.is_data_in_array(response, memes_list), (
                f'Meme was not removed from memes list!\n'
                f'{response}')

    @staticmethod
    def check_message_after_meme_deleting(mem_id, response):
        with allure.step('Check message after meme deleting'):
            exp_message = f'Meme with id {mem_id} successfully deleted'
            assert exp_message == response, (f'Incorrect message!\n'
                                             f'Exp: {exp_message}\n'
                                             f'Act: {response}')
