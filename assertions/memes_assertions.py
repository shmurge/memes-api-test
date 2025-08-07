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
        with allure.step('Проверка данных мема'):
            self.check_data_is_equal(payload.text, response.text)
            self.check_data_is_equal(payload.url, response.url)
            self.check_data_is_equal(payload.tags, response.tags)
            self.check_data_is_equal(payload.info, response.info)
            self.check_data_is_equal(self.username, response.updated_by)

    def id_should_not_change(self, exp_id, act_id):
        with allure.step('ID мема не изменился'):
            self.check_data_is_equal(exp_id, act_id)

    def meme_should_not_be_found(self, mem_id):
        with allure.step(f"Мем с id {mem_id} не был найден!"):
            resp = requests.get(
                url=f"{self.endpoints.get_all_memes}/{mem_id}",
                headers=self.headers.headers_with_auth()
            )

            self.check_status_code_is_404(resp)

    def meme_should_be_in_list(self, memes_list, response):
        with allure.step('Мем отображается в списке'):
            assert self.is_data_in_array(response, memes_list), (f'Мем не найден в списке!\n'
                                                                 f'{response}')

            for meme in memes_list:
                if meme.id == response.id:
                    self.check_meme_fields(meme, response)
                    break

    def meme_should_not_be_in_list(self, memes_list, response):
        with allure.step('Мем не отображается в списке'):
            assert not self.is_data_in_array(response, memes_list), (
                f'Мем не был удален из списка!\n'
                f'{response}')

    @staticmethod
    def check_message_after_meme_deleting(mem_id, response):
        with allure.step('Отображается сообщение об успешном удалении мема'):
            exp_message = f'Meme with id {mem_id} successfully deleted'
            assert exp_message == response, (f'Некорректное сообщение!\n'
                                             f'ОР: {exp_message}\n'
                                             f'ФР: {response}')
