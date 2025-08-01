from api_client.base_endpoints import BaseEndpoints

HOST = BaseEndpoints.HOST


class MemesEndpoints:
    create_meme = f"{HOST}/meme"
    get_all_memes = f"{HOST}/meme"
