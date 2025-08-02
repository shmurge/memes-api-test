import allure
import pytest
from config.base_test import BaseTest
from api_client.memes_api.payloads import MemesPayloads


payload = MemesPayloads()


class TestMemes(BaseTest):

    def test_create_meme(self):
        create_meme_resp = self.memes_api.create_meme(payload.create_meme)
        get_meme_resp = self.memes_api.get_meme_by_id(create_meme_resp.id)

        self.memes_api.assertions.check_meme_fields(create_meme_resp, get_meme_resp)

    def test_update_meme(self, pre_create_and_delete_meme):
        mem_id = pre_create_and_delete_meme.id
        update_meme_resp = self.memes_api.update_meme(mem_id, payload.update_meme(mem_id))
        get_meme_resp = self.memes_api.get_meme_by_id(update_meme_resp.id)

        self.memes_api.assertions.check_meme_fields(update_meme_resp, get_meme_resp)

    def test_delete_meme(self, pre_create_meme):
        mem_id = pre_create_meme.id
        self.memes_api.delete_meme(mem_id)

        self.memes_api.meme_should_not_be_found(mem_id)