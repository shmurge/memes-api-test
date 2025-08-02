from api_client.memes_api.memes_api import MemesApi


class BaseTest:

    def setup_method(self):
        self.memes_api = MemesApi()
