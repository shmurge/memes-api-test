import allure
import pytest
from config.base_test import BaseTest


class TestMemes(BaseTest):

    def test_create_meme(self):
        self.memes_api.create_meme()

    def test_one(self):
        pass