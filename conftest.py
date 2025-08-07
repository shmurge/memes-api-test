import allure
import pytest
import os
from dotenv import load_dotenv, set_key
from api_client.base_api import BaseApi
from api_client.base_endpoints import BaseEndpoints
from api_client.base_models import RequestAuthorizationModel
from api_client.memes_api.payloads import MemesPayloads
from api_client.memes_api.memes_api import MemesApi


def set_env_key(key, value):
    project_root = os.path.dirname(os.path.abspath(__file__))  # путь к директории текущего файла
    env_path = os.path.join(project_root, '.env')  # соединяем с именем файла .env

    load_dotenv(env_path)

    os.environ[key] = value
    set_key(env_path, key, value)


HOST = BaseEndpoints.HOST


@pytest.fixture(autouse=True, scope='session')
def check_token():
    with allure.step('Получение апи токена'):
        token = os.getenv('API-TOKEN')
        username = os.getenv('USERNAME')
        if token:
            if not BaseApi().api_token_is_alive(token):
                resp = BaseApi().user_authorization(RequestAuthorizationModel(
                    name=username))
                set_env_key('API-TOKEN', resp.token)
        else:
            resp = BaseApi().user_authorization(RequestAuthorizationModel(
                name=username))
            set_env_key('API-TOKEN', resp.token)


@pytest.fixture()
def pre_create_meme():
    return MemesApi().create_meme(MemesPayloads().create_meme())


@pytest.fixture()
def pre_create_and_delete_meme():
    req = MemesApi().create_meme(MemesPayloads().create_meme())

    yield req

    MemesApi().delete_meme(req.id)


@pytest.fixture()
def pre_update_meme():
    req = MemesApi().create_meme(MemesPayloads().create_meme())

    return MemesApi().update_meme(req.id, MemesPayloads().update_meme(req.id))


@pytest.fixture()
def pre_update_and_delete_meme():
    req_1 = MemesApi().create_meme(MemesPayloads().create_meme())
    req_2 = MemesApi().update_meme(req_1.id, MemesPayloads().update_meme(req_1.id))

    yield req_2

    MemesApi().delete_meme(req_2.id)
