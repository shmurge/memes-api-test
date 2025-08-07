from api_client.base_api import BaseApi
from api_client.memes_api.memes_api import MemesApi


class BaseTest:

    def setup_method(self):
        self.base_api = BaseApi()
        self.memes_api = MemesApi()
