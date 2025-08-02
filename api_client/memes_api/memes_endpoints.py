from api_client.base_endpoints import BaseEndpoints

HOST = BaseEndpoints.HOST


class MemesEndpoints:
    create_meme = f"{HOST}/meme"
    update_meme = lambda self, meme_id: f"{HOST}/meme/{meme_id}"
    get_all_memes = f"{HOST}/meme"
    delete_meme = lambda self, meme_id: f"{HOST}/meme/{meme_id}"
