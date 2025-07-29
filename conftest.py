import pytest
import os
from dotenv import load_dotenv, set_key
from http_client.endpoints.base_endpoint import BaseEndpoint
from http_client.models.base_models import RequestAuthorizationModel


def set_env_key(key, value):
    project_root = os.path.dirname(os.path.abspath(__file__))  # путь к директории текущего файла
    env_path = os.path.join(project_root, '.env')  # соединяем с именем файла .env

    load_dotenv(env_path)

    set_key(env_path, key, value)


#set_env_key('USERNAME', '')
#set_env_key('API-TOKEN', '')

HOST = 'http://memesapi.course.qa-practice.com'


@pytest.fixture(scope='session', autouse=True)
def check_token():
    token = os.getenv('API-TOKEN')
    if token:
        print(BaseEndpoint().api_token_is_alive(token))
    else:
        username = os.getenv('USERNAME')
        resp = BaseEndpoint().user_authorization(RequestAuthorizationModel(
            name=username))
        set_env_key('API-TOKEN', resp.token)
