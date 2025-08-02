import allure
import os
from dotenv import load_dotenv

from assertions.base_assertions import BaseAssertions

load_dotenv()


class MemesAssertions(BaseAssertions):

    def __init__(self):
        super().__init__()

        self.username = os.getenv('USERNAME')

    def check_meme_fields(self, payload, response):
        with allure.step('Check meme creation'):
            self.check_data_is_equal(payload.text, response.text)
            self.check_data_is_equal(payload.url, response.url)
            self.check_data_is_equal(payload.tags, response.tags)
            self.check_data_is_equal(payload.info, response.info)
            self.check_data_is_equal(self.username, response.updated_by)

    def id_should_not_change(self, exp_id, act_id):
        with allure.step('Meme id should not change'):
            self.check_data_is_equal(exp_id, act_id)
